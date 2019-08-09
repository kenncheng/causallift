def parameters_():
    args = dict(
        cols_features=None,
        col_treatment="Treatment",
        col_outcome="Outcome",
        col_propensity="Propensity",
        col_cate="CATE",
        col_recommendation="Recommendation",
        min_propensity=0.01,
        max_propensity=0.99,
        random_state=0,
        verbose=2,
        uplift_model_params={
            "max_depth": [3],
            "learning_rate": [0.1],
            "n_estimators": [100],
            "verbose": [0],
            "objective": ["binary:logistic"],
            "booster": ["gbtree"],
            "n_jobs": [-1],
            "nthread": [None],
            "gamma": [0],
            "min_child_weight": [1],
            "max_delta_step": [0],
            "subsample": [1],
            "colsample_bytree": [1],
            "colsample_bylevel": [1],
            "reg_alpha": [0],
            "reg_lambda": [1],
            "scale_pos_weight": [1],
            "base_score": [0.5],
            "missing": [None],
        },
        enable_ipw=True,
        propensity_model_params={
            "C": [0.1, 1, 10],
            "class_weight": [None],
            "dual": [False],
            "fit_intercept": [True],
            "intercept_scaling": [1],
            "max_iter": [100],
            "multi_class": ["ovr"],
            "n_jobs": [1],
            "penalty": ["l1", "l2"],
            "solver": ["liblinear"],
            "tol": [0.0001],
            "warm_start": [False],
        },
        cv=3,
        index_name="index",
        partition_name="partition",
        runner="SequentialRunner",  # 'ParallelRunner' # None
        conditionally_skip=False,
    )
    return args
