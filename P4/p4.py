                                                                                                                                                                                                      
# Before you get started, please tell us who you are, putting your
# Net ID and your partner's Net ID below (or none if your working solo)                                                                                                                                      
#
# project: p4
# submitter: wxia9
# partner: none
import pandas as pd

def predict1(glucose, bmi, age):
    '''predict1 implements a decision tree of depth 1. It takes as input
    glucose, bmi, and age.  It returns True (corresponding to class=1
    in the tree) to forecast the patient is likely to get diabetes,
    and False (corresponding to class=0 in the tree) otherwise.
    '''

    # TODO: uncomment and finish the conditional:

    if glucose <= 127.5:
        return False
    else:
        return True


def predict2(glucose, bmi, age):
    '''predict2 implements a decision tree of depth 2. It takes as input
    glucose, bmi, and age.  It returns True (corresponding to class=1
    in the tree) to forecast the patient is likely to get diabetes,
    and False (corresponding to class=0 in the tree) otherwise.
    '''
    if predict1(glucose, bmi, age) :
        if bmi <= 29.95: 
            return False;
        else :
            return True;
    else :
        return False;


def predict3(glucose=None, bmi=None, age=None):
    '''predict3 implements a decision tree of depth 3. It takes as input
    glucose, bmi, and age.  It returns True (corresponding to class=1
    in the tree) to forecast the patient is likely to get diabetes,
    and False (corresponding to class=0 in the tree) otherwise.
    '''

    # TODO: for the challenge questions, get rid of this check, and
    # replace None values with the average for the population, using
    # the column_avg function you'll complete
    if glucose == None: glucose = column_avg("glucose")
    if bmi == None: bmi = column_avg("bmi")
    if age == None: age = column_avg("age")
    
    if glucose <= 127.5:
        if age <= 28.5: 
            if bmi <= 45.4: 
                return False
            else: 
                return True
        else: 
            return False
    else: 
        if bmi <= 29.95:
            if glucose <= 145.5:
                return False
            else:
                return True
        else:
            return True
        


def column_avg(column_name):
    '''if column_name is "glucose" it will return the average glucose
    level across patients in the dataset.  If column_name is "bmi", it
    return the average bmi, and so on

    '''

    # TODO: divide the sum of the column by the number of rows to get
    # the average value in the column.
    #
    # you can call column_sum and row_count below to get the numerator
    # and denominator to compute the average
    if column_name == "glucose":
        return column_sum(column_name)/row_count()
    if column_name == "bmi":
        return column_sum(column_name)/row_count()
    if column_name == "age":
        return column_sum(column_name)/row_count()
    if column_name == "pregnancies":
        return column_sum(column_name)/row_count()
    if column_name == "bp":
        return column_sum(column_name)/row_count()
    if column_name == "insulin":
        return column_sum(column_name)/row_count()
    if column_name == "pedigree":
        return column_sum(column_name)/row_count()
    if column_name == "skin":
        return column_sum(column_name)/row_count()
    return


# the following functions do some things we haven't covered in class
# yet.
#
# you will use them to implement column_avg, but you don't need to
# understand how they work as they do at this point in the semester.

dataset = pd.read_csv("diabetes.csv")


def column_sum(column_name):
    return dataset[column_name].sum()


def row_count():
    return len(dataset)
