# -*- coding: utf-8 -*-

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

from sklearn_porter import Porter


iris_data = load_iris()
X, y = iris_data.data, iris_data.target
clf = KNeighborsClassifier(algorithm='brute', n_neighbors=3, weights='uniform')
clf.fit(X, y)

# Cheese!

result = Porter(clf).export()
# model = Porter(clf, language='java').export()
print(result)

"""
import java.util.*;

class Brain {

    private static class Neighbor {
        Integer clazz;
        Double dist;
        public Neighbor(int clazz, double dist) {
            this.clazz = clazz;
            this.dist = dist;
        }
    }

    public static double compDist(double[] temp, double[] cand, double q) {
        double dist = 0.;
        double diff;
        for (int i = 0, l = temp.length; i < l; i++) {
    	    diff = Math.abs(temp[i] - cand[i]);
    	    if (q==1) {
    	        dist += diff;
    	    } else if (q==2) {
    	        dist += diff*diff;
    	    } else if (q==Double.POSITIVE_INFINITY) {
    	        if (diff > dist) {
    	            dist = diff;
    	        }
    	    } else {
    	        dist += Math.pow(diff, q);
    		}
        }
        if (q==1 || q==Double.POSITIVE_INFINITY) {
            return dist;
        } else if (q==2) {
            return Math.sqrt(dist);
        } else {
            return Math.pow(dist, 1. / q);
        }
    }

    public static int predict(double[] atts) {
        if (atts.length != 4) {
            return -1;
        }

        double[][] X = {{5.0999999999999996, 3.5, 1.3999999999999999, 0.20000000000000001}, {4.9000000000000004, 3.0, 1.3999999999999999, 0.20000000000000001}, {4.7000000000000002, 3.2000000000000002, 1.3, 0.20000000000000001}, {4.5999999999999996, 3.1000000000000001, 1.5, 0.20000000000000001}, {5.0, 3.6000000000000001, 1.3999999999999999, 0.20000000000000001}, {5.4000000000000004, 3.8999999999999999, 1.7, 0.40000000000000002}, {4.5999999999999996, 3.3999999999999999, 1.3999999999999999, 0.29999999999999999}, {5.0, 3.3999999999999999, 1.5, 0.20000000000000001}, {4.4000000000000004, 2.8999999999999999, 1.3999999999999999, 0.20000000000000001}, {4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001}, {5.4000000000000004, 3.7000000000000002, 1.5, 0.20000000000000001}, {4.7999999999999998, 3.3999999999999999, 1.6000000000000001, 0.20000000000000001}, {4.7999999999999998, 3.0, 1.3999999999999999, 0.10000000000000001}, {4.2999999999999998, 3.0, 1.1000000000000001, 0.10000000000000001}, {5.7999999999999998, 4.0, 1.2, 0.20000000000000001}, {5.7000000000000002, 4.4000000000000004, 1.5, 0.40000000000000002}, {5.4000000000000004, 3.8999999999999999, 1.3, 0.40000000000000002}, {5.0999999999999996, 3.5, 1.3999999999999999, 0.29999999999999999}, {5.7000000000000002, 3.7999999999999998, 1.7, 0.29999999999999999}, {5.0999999999999996, 3.7999999999999998, 1.5, 0.29999999999999999}, {5.4000000000000004, 3.3999999999999999, 1.7, 0.20000000000000001}, {5.0999999999999996, 3.7000000000000002, 1.5, 0.40000000000000002}, {4.5999999999999996, 3.6000000000000001, 1.0, 0.20000000000000001}, {5.0999999999999996, 3.2999999999999998, 1.7, 0.5}, {4.7999999999999998, 3.3999999999999999, 1.8999999999999999, 0.20000000000000001}, {5.0, 3.0, 1.6000000000000001, 0.20000000000000001}, {5.0, 3.3999999999999999, 1.6000000000000001, 0.40000000000000002}, {5.2000000000000002, 3.5, 1.5, 0.20000000000000001}, {5.2000000000000002, 3.3999999999999999, 1.3999999999999999, 0.20000000000000001}, {4.7000000000000002, 3.2000000000000002, 1.6000000000000001, 0.20000000000000001}, {4.7999999999999998, 3.1000000000000001, 1.6000000000000001, 0.20000000000000001}, {5.4000000000000004, 3.3999999999999999, 1.5, 0.40000000000000002}, {5.2000000000000002, 4.0999999999999996, 1.5, 0.10000000000000001}, {5.5, 4.2000000000000002, 1.3999999999999999, 0.20000000000000001}, {4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001}, {5.0, 3.2000000000000002, 1.2, 0.20000000000000001}, {5.5, 3.5, 1.3, 0.20000000000000001}, {4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001}, {4.4000000000000004, 3.0, 1.3, 0.20000000000000001}, {5.0999999999999996, 3.3999999999999999, 1.5, 0.20000000000000001}, {5.0, 3.5, 1.3, 0.29999999999999999}, {4.5, 2.2999999999999998, 1.3, 0.29999999999999999}, {4.4000000000000004, 3.2000000000000002, 1.3, 0.20000000000000001}, {5.0, 3.5, 1.6000000000000001, 0.59999999999999998}, {5.0999999999999996, 3.7999999999999998, 1.8999999999999999, 0.40000000000000002}, {4.7999999999999998, 3.0, 1.3999999999999999, 0.29999999999999999}, {5.0999999999999996, 3.7999999999999998, 1.6000000000000001, 0.20000000000000001}, {4.5999999999999996, 3.2000000000000002, 1.3999999999999999, 0.20000000000000001}, {5.2999999999999998, 3.7000000000000002, 1.5, 0.20000000000000001}, {5.0, 3.2999999999999998, 1.3999999999999999, 0.20000000000000001}, {7.0, 3.2000000000000002, 4.7000000000000002, 1.3999999999999999}, {6.4000000000000004, 3.2000000000000002, 4.5, 1.5}, {6.9000000000000004, 3.1000000000000001, 4.9000000000000004, 1.5}, {5.5, 2.2999999999999998, 4.0, 1.3}, {6.5, 2.7999999999999998, 4.5999999999999996, 1.5}, {5.7000000000000002, 2.7999999999999998, 4.5, 1.3}, {6.2999999999999998, 3.2999999999999998, 4.7000000000000002, 1.6000000000000001}, {4.9000000000000004, 2.3999999999999999, 3.2999999999999998, 1.0}, {6.5999999999999996, 2.8999999999999999, 4.5999999999999996, 1.3}, {5.2000000000000002, 2.7000000000000002, 3.8999999999999999, 1.3999999999999999}, {5.0, 2.0, 3.5, 1.0}, {5.9000000000000004, 3.0, 4.2000000000000002, 1.5}, {6.0, 2.2000000000000002, 4.0, 1.0}, {6.0999999999999996, 2.8999999999999999, 4.7000000000000002, 1.3999999999999999}, {5.5999999999999996, 2.8999999999999999, 3.6000000000000001, 1.3}, {6.7000000000000002, 3.1000000000000001, 4.4000000000000004, 1.3999999999999999}, {5.5999999999999996, 3.0, 4.5, 1.5}, {5.7999999999999998, 2.7000000000000002, 4.0999999999999996, 1.0}, {6.2000000000000002, 2.2000000000000002, 4.5, 1.5}, {5.5999999999999996, 2.5, 3.8999999999999999, 1.1000000000000001}, {5.9000000000000004, 3.2000000000000002, 4.7999999999999998, 1.8}, {6.0999999999999996, 2.7999999999999998, 4.0, 1.3}, {6.2999999999999998, 2.5, 4.9000000000000004, 1.5}, {6.0999999999999996, 2.7999999999999998, 4.7000000000000002, 1.2}, {6.4000000000000004, 2.8999999999999999, 4.2999999999999998, 1.3}, {6.5999999999999996, 3.0, 4.4000000000000004, 1.3999999999999999}, {6.7999999999999998, 2.7999999999999998, 4.7999999999999998, 1.3999999999999999}, {6.7000000000000002, 3.0, 5.0, 1.7}, {6.0, 2.8999999999999999, 4.5, 1.5}, {5.7000000000000002, 2.6000000000000001, 3.5, 1.0}, {5.5, 2.3999999999999999, 3.7999999999999998, 1.1000000000000001}, {5.5, 2.3999999999999999, 3.7000000000000002, 1.0}, {5.7999999999999998, 2.7000000000000002, 3.8999999999999999, 1.2}, {6.0, 2.7000000000000002, 5.0999999999999996, 1.6000000000000001}, {5.4000000000000004, 3.0, 4.5, 1.5}, {6.0, 3.3999999999999999, 4.5, 1.6000000000000001}, {6.7000000000000002, 3.1000000000000001, 4.7000000000000002, 1.5}, {6.2999999999999998, 2.2999999999999998, 4.4000000000000004, 1.3}, {5.5999999999999996, 3.0, 4.0999999999999996, 1.3}, {5.5, 2.5, 4.0, 1.3}, {5.5, 2.6000000000000001, 4.4000000000000004, 1.2}, {6.0999999999999996, 3.0, 4.5999999999999996, 1.3999999999999999}, {5.7999999999999998, 2.6000000000000001, 4.0, 1.2}, {5.0, 2.2999999999999998, 3.2999999999999998, 1.0}, {5.5999999999999996, 2.7000000000000002, 4.2000000000000002, 1.3}, {5.7000000000000002, 3.0, 4.2000000000000002, 1.2}, {5.7000000000000002, 2.8999999999999999, 4.2000000000000002, 1.3}, {6.2000000000000002, 2.8999999999999999, 4.2999999999999998, 1.3}, {5.0999999999999996, 2.5, 3.0, 1.1000000000000001}, {5.7000000000000002, 2.7999999999999998, 4.0999999999999996, 1.3}, {6.2999999999999998, 3.2999999999999998, 6.0, 2.5}, {5.7999999999999998, 2.7000000000000002, 5.0999999999999996, 1.8999999999999999}, {7.0999999999999996, 3.0, 5.9000000000000004, 2.1000000000000001}, {6.2999999999999998, 2.8999999999999999, 5.5999999999999996, 1.8}, {6.5, 3.0, 5.7999999999999998, 2.2000000000000002}, {7.5999999999999996, 3.0, 6.5999999999999996, 2.1000000000000001}, {4.9000000000000004, 2.5, 4.5, 1.7}, {7.2999999999999998, 2.8999999999999999, 6.2999999999999998, 1.8}, {6.7000000000000002, 2.5, 5.7999999999999998, 1.8}, {7.2000000000000002, 3.6000000000000001, 6.0999999999999996, 2.5}, {6.5, 3.2000000000000002, 5.0999999999999996, 2.0}, {6.4000000000000004, 2.7000000000000002, 5.2999999999999998, 1.8999999999999999}, {6.7999999999999998, 3.0, 5.5, 2.1000000000000001}, {5.7000000000000002, 2.5, 5.0, 2.0}, {5.7999999999999998, 2.7999999999999998, 5.0999999999999996, 2.3999999999999999}, {6.4000000000000004, 3.2000000000000002, 5.2999999999999998, 2.2999999999999998}, {6.5, 3.0, 5.5, 1.8}, {7.7000000000000002, 3.7999999999999998, 6.7000000000000002, 2.2000000000000002}, {7.7000000000000002, 2.6000000000000001, 6.9000000000000004, 2.2999999999999998}, {6.0, 2.2000000000000002, 5.0, 1.5}, {6.9000000000000004, 3.2000000000000002, 5.7000000000000002, 2.2999999999999998}, {5.5999999999999996, 2.7999999999999998, 4.9000000000000004, 2.0}, {7.7000000000000002, 2.7999999999999998, 6.7000000000000002, 2.0}, {6.2999999999999998, 2.7000000000000002, 4.9000000000000004, 1.8}, {6.7000000000000002, 3.2999999999999998, 5.7000000000000002, 2.1000000000000001}, {7.2000000000000002, 3.2000000000000002, 6.0, 1.8}, {6.2000000000000002, 2.7999999999999998, 4.7999999999999998, 1.8}, {6.0999999999999996, 3.0, 4.9000000000000004, 1.8}, {6.4000000000000004, 2.7999999999999998, 5.5999999999999996, 2.1000000000000001}, {7.2000000000000002, 3.0, 5.7999999999999998, 1.6000000000000001}, {7.4000000000000004, 2.7999999999999998, 6.0999999999999996, 1.8999999999999999}, {7.9000000000000004, 3.7999999999999998, 6.4000000000000004, 2.0}, {6.4000000000000004, 2.7999999999999998, 5.5999999999999996, 2.2000000000000002}, {6.2999999999999998, 2.7999999999999998, 5.0999999999999996, 1.5}, {6.0999999999999996, 2.6000000000000001, 5.5999999999999996, 1.3999999999999999}, {7.7000000000000002, 3.0, 6.0999999999999996, 2.2999999999999998}, {6.2999999999999998, 3.3999999999999999, 5.5999999999999996, 2.3999999999999999}, {6.4000000000000004, 3.1000000000000001, 5.5, 1.8}, {6.0, 3.0, 4.7999999999999998, 1.8}, {6.9000000000000004, 3.1000000000000001, 5.4000000000000004, 2.1000000000000001}, {6.7000000000000002, 3.1000000000000001, 5.5999999999999996, 2.3999999999999999}, {6.9000000000000004, 3.1000000000000001, 5.0999999999999996, 2.2999999999999998}, {5.7999999999999998, 2.7000000000000002, 5.0999999999999996, 1.8999999999999999}, {6.7999999999999998, 3.2000000000000002, 5.9000000000000004, 2.2999999999999998}, {6.7000000000000002, 3.2999999999999998, 5.7000000000000002, 2.5}, {6.7000000000000002, 3.0, 5.2000000000000002, 2.2999999999999998}, {6.2999999999999998, 2.5, 5.0, 1.8999999999999999}, {6.5, 3.0, 5.2000000000000002, 2.0}, {6.2000000000000002, 3.3999999999999999, 5.4000000000000004, 2.2999999999999998}, {5.9000000000000004, 3.0, 5.0999999999999996, 1.8}};
        int[] y = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2};

        int classIdx = -1;
        int nNeighbors = 3;
        int nTemplates = 150;
        int nClasses = 3;
        double power = 2;

        if (nNeighbors == 1) {
            double minDist = Double.POSITIVE_INFINITY;
            double curDist;
            for (int i = 0; i < nTemplates; i++) {
                curDist = Brain.compDist(X[i], atts, power);
                if (curDist <= minDist) {
                    minDist = curDist;
                    classIdx = y[i];
                }
            }
        } else {
            int[] classes = new int[nClasses];
            ArrayList<Neighbor> dists = new ArrayList<Neighbor>();
            for (int i = 0; i < nTemplates; i++) {
                dists.add(new Neighbor(y[i], Brain.compDist(X[i], atts, power)));
            }
            Collections.sort(dists, new Comparator<Neighbor>() {
                @Override
                public int compare(Neighbor n1, Neighbor n2) {
                    return n1.dist.compareTo(n2.dist);
                }
            });
            for (Neighbor neighbor : dists.subList(0, nNeighbors)) {
                classes[neighbor.clazz]++;
            }
            int classVal = -1;
            for (int i = 0; i < nClasses; i++) {
                if (classes[i] > classVal) {
                    classVal = classes[i];
                    classIdx = i;
                }
            }
        }
        return classIdx;
    }

    public static void main(String[] args) {
        if (args.length == 4) {
            double[] atts = new double[args.length];
            for (int i = 0, l = args.length; i < l; i++) {
                atts[i] = Double.parseDouble(args[i]);
            }
            System.out.println(Brain.predict(atts));
        }
    }
}
"""
