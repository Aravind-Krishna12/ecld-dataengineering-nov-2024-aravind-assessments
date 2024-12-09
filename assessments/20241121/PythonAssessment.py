import pandas as pd
def load_data(file_):
    with open(file_, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    df = pd.DataFrame(data, columns=['Timestamp', 'IP', 'Status Code', 'Endpoint'])
    return df

def parse_log_line(file_):
    df = load_data(file_)
    return list(df.to_records())

def get_unique_visitors(file_):
    df = load_data(file_)
    return df['IP'].nunique()

def get_popular_endpoints(file_,top_n=5) :
    df = load_data(file_)
    return df['Endpoint'].value_counts().nlargest(top_n)

def get_error_rates(file_):
    df = load_data(file)
    words = df["Status Code"]
    error = df['Status Code'].apply(lambda terms: [word for word in words if any(word.startswith(term) for term in terms)])
    return float(len(error.shape[1])/len(df.shape[1]))  
    
def generate_report(file_):
    parse_log_line(file_)
    unique_visitors = get_unique_visitors(file_)
    popular_end_points = get_popular_endpoints(file_,top_n=5)
    error_rates = get_error_rates(file_)




    print(f"Number of Unique Visitors : {unique_visitors}")
    print(f"Most Accessed End Points are : {popular_end_points}")
    print(f"Error rates are : {error_rates}")
    
    




if __name__ == '__main__':    
    file = 'sample-log.txt'    
    generate_report(file)
