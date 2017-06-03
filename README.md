# Bigdata_analysis_HW2
## Parameter Tuning in XGBoost and GBM

* Tuning GBM parameters: 
1. n_estimators(500): I first try 20 30..80, and I found higher values get highe accuracy. Therefore, I try 50 100..650 and found there is no significant grow after 500, and I predict 500 is the best.(In fact 650 is a bit higher)
2. min_samples_split(200),max_depth(9): test min_sample_split for 200 400..1000 and max_depth for 5 7...15, and I found (200,9) is the best.
3. min_samples_leaf(70):  
4. max_features(8):
5. subsample(0.8):
