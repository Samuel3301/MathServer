from django.shortcuts import render

def churn_rate(request):
    c = int(request.POST.get('initialcust', '0'))
    n= int(request.POST.get('custlost', '0'))

    churn_rate = (c /n) * 100 if request.method == 'POST' else 0

    print("initial_cust =", c)
    print("custlost =", n)
    print("churn_rate =", churn_rate)

    return render(
        request,
        'rajapp/math.html',
        {'initial_cust': c, 'custlost': n, 'churn_rate': churn_rate}
    )
