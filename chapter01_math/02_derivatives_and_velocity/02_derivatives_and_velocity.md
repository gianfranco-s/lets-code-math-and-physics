## What is a derivative?
You might be thinking about a weird calculus limit. That's okay, but let's get the Physics angle. Suppose a car's position is described as
```
x(t) = t^3
```
Why? Well, because not every movement has uniform acceleration.

How would you describe the car's velocity? This concept requires us to compare two instants: the "now" -let's call it *t*, and the "future" -let's call it *t+dt*. Note that the "future" is the "now" plus a short interval *dt*. To calculate the velocity, we'll need to compute where the car will be in the future with respect to where it is now, the distance:
```
x(t+dt) - x(t)
```
We also want to calculate how long it took to get from the "now" to the "future", like this: "future"-"now"
```
(t+dt)-(t) = dt
```

Finally the velocity is calculated as distance over time:
```
v = [ x(t+dt) - x(t) ] / dt
```

You've seen this expression in every calculus book. There's nothing magical about it...  
Actually, there IS some magic; and it happens when we take a closer look to *dt*.

1. Let's plot an awful derivative. It's not really a derivative, but we'll get there. Run `plot_an_awful_derivative.ipynb`

2. Now, let's plot better approximations in `plot_a_decent_derivative.py`

3. Finally, let's improve our software skills. This will become handy in the future. We'll repeat what we did before, but with *functions*.
