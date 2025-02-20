from django.shortcuts import render
from .utils import encrypt_text, decrypt_text

def home(request):
    return render(request, 'crypto/home.html')

def encrypt_view(request):
    encrypted_message = None
    encryption_key = None
    if request.method == 'POST':
        text = request.POST.get('text', '')
        encrypted_message, encryption_key = encrypt_text(text)
        # Render result.html only if text is entered
        return render(request, 'crypto/result.html', {'result': encrypted_message, 'encryption_key': encryption_key})
    
    # If no form submission, just render the encrypt page
    return render(request, 'crypto/encrypt.html')

def decrypt_view(request):
    decrypted_message = None
    if request.method == 'POST':
        encrypted_text = request.POST.get('text', '')
        key = request.POST.get('key', '')
        if encrypted_text and key:
            try:
                decrypted_message = decrypt_text(encrypted_text, key)
            except Exception:
                decrypted_message = "Invalid encryption key or message."
        # Render result.html only if decryption is successful
        return render(request, 'crypto/result.html', {'result': decrypted_message})
    
    # If no form submission, just render the decrypt page
    return render(request, 'crypto/decrypt.html')
