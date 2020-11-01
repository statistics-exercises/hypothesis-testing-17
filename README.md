# p-values for two-tail tests

In the previous two exercises, you have used the new flowchart shown below to report the result of a hypothesis test for the two kinds of one-tail test.  In this exercise, we are thus going to use this method to perform a two-tail test.

![](hypo-testing.003.jpeg)

I have once again provided you with some data in the file `mydata.dat` that may or not be a series of samples from a normal distribution with expectation 3 and standard devotion 4.   You should perform a hypothesis test with the following null and hypothesis tests:

1. __null hypothesis__: The distribution that was sampled has an expectation of 3
2. __alternative hypothesis__: The distribution that was sampled has an expectation that not equal to 3

To get you started I have written the functions completed in the previous task:

1. `testStatistic` - Three variables are passed to this function.  `data` is a NumPy array that contains N normal random variables, `mu` is the value of the expectation for the distribution that is assumed under the null hypothesis and `sigma` is the square root of the variance for the distribution.  This function should calculate and return the test statistic:

![](https://render.githubusercontent.com/render/math?math=T=\frac{1}{\sigma\sqrt{n}}\sum_{i=1}^{n}(X_i-\mu_0))

2. `pvalue` - Three variables are passed to this function.  `data` is a NumPy array that contains N normal random variables, `mu` is the value of the expectation for the distribution that is assumed under the null hypothesis and `sigma` is the square root of the variance for the distribution.  The function calls `testStatistic` to evaluate T using the formula above.  You should modify it so that the function returns the __p-value__ based on the value of the __statistic__

Hint: When calculating the __p-value__ for a two-tail test you need to consider that the critical region has two disjoint parts when we do this type of test.
