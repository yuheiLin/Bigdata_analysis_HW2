# Bigdata_analysis_HW2
## Parameter Tuning in GBM

* Tuning GBM parameters: 
 1. n_estimators(500): <br>I first try 20 30..80, and I found higher values get highe accuracy. Therefore, I try 50 100..650 and found there is no significant grow after 500, and I predict 500 is the best.(In fact 650 is a bit higher) 
 2. min_samples_split(200),max_depth(9): <br>Test min_sample_split for 200 400..1000 and max_depth for 5 7...15, and I found (200,9) is the best.
 3. min_samples_leaf(70): <br> Test 30 40...190, and 70 is the best.
 4. max_features(8): <br> Test 2,4,6,8,10 and 8 is the best.
 5. subsample(0.8): <br> 0.6 0.65....0.9 and 0.8 is the best.
* Base_on : <br>都只有使用dataset前10個featrue，因為用過多feature準確率會高於99%甚至100%，太少則低於90%
* Result : （調整過程沒畫Heatmap，有存在GBM_tuning.txt）<br>若不條任何參數(default) CV Score : Mean - 0.9645751 | Std - 0.002323271 <br>調整參數後 CV Score : Mean - 0.9763546 | Std - 0.001681305 <br> 平均減少1.2%的錯誤
* Summary : <br>n_estimators設500有點偏高，所以導致之後再測其他最佳參數時花較多的時間，基本設(n_estimators=500,learning_rate=0.2)去測其他參數，0.2是為了減少時間，之後若遇到更大的Dataset可能最高n_estimators=100,leaning_rate=0.2去優化其他參數

## Parameter Tuning in XGBoost
will be update soon...
