# Features selected from intialliy processed dataset
SELECTED_FEATURES = [
    'loan_amnt',
    'term',
    'int_rate',
    'grade',
    'home_ownership',
    'annual_inc',
    'verification_status',
    'dti',
    'fico_range_low',
    'open_acc',
    'revol_bal',
    'initial_list_status',
    'application_type',
    'acc_now_delinq',
    'acc_open_past_24mths',
    'avg_cur_bal',
    'bc_util',
    'disbursement_method',
    'target'
]

# Date format features
DATE_FEATURES = ['issue_d', 'last_pymnt_d', 'last_credit_pull_d']

# Features selected for binary encoding
BINARY_FEATURES = ['term', 'initial_list_status', 'application_type', 'disbursement_method']

# Features selected for one-hot encoding
CATEGORY_FEATURES = ['grade', 'home_ownership', 'verification_status']
