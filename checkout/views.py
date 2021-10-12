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
        'stripe_public_key': 'pk_test_51Jjk1tLoLAoW8DAN10Tq5Xp5CBLIZY5qtME8l17V730Xny2itpGUaMyEsKUWXkGAyneRPTe2htn7Nu7H4WoSURQ000PV6hiaFn',
        'client_secret': 'Test Client Secret',
    }

    return render(request, template, context)
