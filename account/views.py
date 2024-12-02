from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import requests
import openai
from django.conf import settings
from .forms import ChangeUsernameForm, QueryForm

openai.api_key = settings.OPENAI_API_KEY

@login_required
def account_page(request):

    chatbot_response = None
    chatbot_form = None

    if request.method == "POST" and 'new_username' in request.POST:
        username_form = ChangeUsernameForm(request.POST)
        if username_form.is_valid():
            new_username = username_form.cleaned_data['new_username']
            request.user.username = new_username
            request.user.save()
            messages.success(request, "Username updated successfully!")
            return redirect('account:account_page')
    else:
        username_form = ChangeUsernameForm()

    if request.method == "POST" and 'old_password' in request.POST:
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in!
            messages.success(request, "Password updated successfully!")
            return redirect('account:account_page')
    else:
        password_form = PasswordChangeForm(user=request.user)

    if request.method == "POST":
        query = request.POST.get('query', '')
        query = f"Generate some names with a life path number of {query}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an assistant specialized in Chaldean Numerology and life path numbers. Provide answers that are concise and accurate."},
                    {"role": "user", "content": query},
                ],
            )
            chatbot_response = response['choices'][0]['message']['content']
        except Exception as e:
            chatbot_response = f"Error communicating with Chatbot: {str(e)}"
    else:
        chatbot_form = QueryForm() # instantiate empty form

    # pass context to template
    context = {
        'username_form': username_form,
        'password_form': password_form,
        'chatbot_form': chatbot_form,
        'chatbot_response': chatbot_response,
    }
    return render(request, 'account/account.html', context)


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login:signup')  
    else:
        return redirect('account:account_page')