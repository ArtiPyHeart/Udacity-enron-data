#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

if __name__ == '__main__':
    ceo = 'Skilling Jeffrey K'.upper()
    president = 'LAY KENNETH L'
    cfo = 'FASTOW ANDREW S'
    print enron_data

    # print enron_data[ceo]
    # print enron_data[president]
    # print enron_data[cfo]

    # with_salary = {}
    # with_email = {}
    # for name in enron_data.keys():
    #     if enron_data[name]['salary'] != 'NaN':
    #         with_salary[name] = enron_data[name]
    #     if enron_data[name]['email_address'] != 'NaN':
    #         with_email[name] = enron_data[name]
    # print len(with_salary)
    # print len(with_email)

    pois = {}
    for name in enron_data.keys():
        if enron_data[name]['poi'] is True:
            pois[name] = enron_data[name]
    print len(pois)
    pois_count = 0
    total_count = 0
    for name in enron_data.keys():
        if enron_data[name]['total_payments'] == 'NaN':
            total_count += 1
    print total_count
    for name in pois.keys():
        if pois[name]['total_payments'] == 'NaN':
            pois_count += 1
    print pois_count