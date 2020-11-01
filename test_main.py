import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_statistic(self) : 
        for n in range(1,21) :
            mu, sigma = -10 +n, 0.1*n
            samples = np.random.normal(mu, sigma, size=20*n )
            stat = ( sum(samples) / (20*n) - mu ) / ( sigma / np.sqrt(n*20) )
            self.assertTrue( np.abs( stat - testStatistic( samples, mu, sigma) )<1e-7, "your function for computing the test statistic is not working correctly" )
            
    def test_pvalue(self) : 
        for n in range(1,21) :
            mu, sigma = -10 +n, 0.1*n
            samples = np.random.normal(mu, sigma, size=20*n )
            stat = testStatistic( samples, mu, sigma )
            if stat>0 : pval = 2*scipy.stats.norm.cdf(-stat)
            else : pval = 2*scipy.stats.norm.cdf(stat)
            self.assertTrue( np.abs( pval - pvalue( samples, mu, sigma ) )<1e-7, "your function for computing the pvalue is not working correctly" )

        stat = testStatistic( data, 3, 4 )
        if stat>0 : pval = 2*scipy.stats.norm.cdf(-stat)
        else : pval = 2*scipy.stats.norm.cdf(stat)
        self.assertTrue( np.abs( pval - pvalue( data, 3, 4 ) )<1e-7, ""your function for computing the pvalue is not working correctly" )
