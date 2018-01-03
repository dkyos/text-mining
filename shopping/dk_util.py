import numpy as np
import pandas as pd
import logging
import random as rn
import os
import sys

LOG_FILE = './log.txt';
logger = logging.getLogger('mylogger');

def initialize(LOG_LEVEL):
    os.environ['PYTHONHASHSEED'] = '0'
    np.random.seed(123)
    rn.seed(12345)
    
    # CRITICAL, ERROR,, WARNING, INFO, DEBUG, NOTSET
    logger.setLevel(LOG_LEVEL)
    fomatter = logging.Formatter(
        '[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    fileHandler = logging.FileHandler(LOG_FILE)
    fileHandler.setFormatter(fomatter)
    logger.addHandler(fileHandler)

    streamHandler = logging.StreamHandler()
    #streamHandler.setFormatter(fomatter)
    logger.addHandler(streamHandler)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #logger.debug(pd.describe_option('display'))

    #np.set_printoptions(threshold=np.inf)
    np.set_printoptions(threshold='nan')

    return;

def strip_col_name(df):
    # Trim Spaces: Remove Trimming leading and trailing spaces
    for oldColumnName in df:
        newColumnName = oldColumnName.strip()
        df.rename(columns={oldColumnName: newColumnName}, inplace=True)

    return df

def append_df(total_df, df):

    if total_df.empty:
        logger.info("init")
        total_df = df
    else:
        logger.info("append: " + str(total_df.shape) + " + " + str(df.shape))

        for i, j in zip( total_df.columns.tolist(), df.columns.tolist() ):
            if i != j:
                logger.debug("Column Name: " + i + " != " + j);

        # if check DataFrame.append it return new object
        tmp = total_df.append(df, ignore_index=True)[total_df.columns.tolist()]
        total_df = tmp

    logger.info(total_df.shape)

    return total_df

def concat_df(total_df, df):

    if total_df.empty:
        logger.info("init")
        total_df = df
    else:
        logger.info("append: " + str(total_df.shape) + " + " + str(df.shape))

        for i, j in zip( total_df.columns.tolist(), df.columns.tolist() ):
            if i != j:
                logger.debug("Column Name: [%s] != [%s]" % (i, j))

        tmp = pd.concat([total_df, df]
            , axis=0, ignore_index=True)[total_df.columns.tolist()]
        total_df = tmp

    logger.info(total_df.shape)

    return total_df

def save_df(df, name):
    df.to_csv(name, sep='|', encoding='utf-8', index=False)

def save_df_index(df, name):
    df.to_csv(name, sep='|', encoding='utf-8', index=True)

