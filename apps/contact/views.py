from django.shortcuts import render, redirect

from apps.contact.forms import ContactForm

def contact_page_views(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.result = 1313
            form.save()
            return redirect('contact:contacts')
        else:
            errors = []
            print(errors)
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)
            context = {
                "errors": errors,
            }
            return render(request, 'contact.html', context)

    else:
        return render(request, 'contact.html',)
