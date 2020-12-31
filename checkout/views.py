from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I4U07LTDekFYtjly4zXPLAIOR3LD0svrGQDqlRskVyJtptKYjiBLBrCPF6BB4ouUxmbzbQnX6rQQe212x95XlYH005IGcjq7z',
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
