## Do you know what a derivative is?
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

You've seen this expression in every calculus book. We won't get into the math of it... but let's plot how it would look like, for differente values of *dt*
