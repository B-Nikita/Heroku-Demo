{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  experience  test_score  interview_score  salary\n",
      "0        NaN         8.0                9   50000\n",
      "1        NaN         8.0                6   45000\n",
      "2       five         6.0                7   60000\n",
      "3        two        10.0               10   65000\n",
      "4      seven         9.0                6   70000\n",
      "5      three         7.0               10   62000\n",
      "6        ten         NaN                7   72000\n",
      "7     eleven         7.0                8   80000\n"
     ]
    }
   ],
   "source": [
    "# Importing the libraries\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "dataset = pd.read_csv('hiring.csv')\n",
    "print(dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Data Preprocessing\n",
    "dataset['experience'].fillna(0, inplace=True)\n",
    "\n",
    "dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)\n",
    "\n",
    "X = dataset.iloc[:, :3]\n",
    "\n",
    "#Converting words to integer values\n",
    "def convert_to_int(word):\n",
    "    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,\n",
    "                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}\n",
    "    return word_dict[word]\n",
    "\n",
    "X['experience'] = X['experience'].apply(lambda x : convert_to_int(x))\n",
    "y = dataset.iloc[:, -1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[53290.89255945]\n"
     ]
    }
   ],
   "source": [
    "#Splitting Training and Test Set\n",
    "#Since we have a very small dataset, we will train our model with all availabe data.\n",
    "\n",
    "from sklearn.linear_model import LinearRegression\n",
    "regressor = LinearRegression()\n",
    "\n",
    "#Fitting model with trainig data\n",
    "regressor.fit(X, y)\n",
    "\n",
    "# Saving model to disk\n",
    "pickle.dump(regressor, open('model.pkl','wb'))\n",
    "\n",
    "# Loading model to compare the results\n",
    "model = pickle.load(open('model.pkl','rb'))\n",
    "print(model.predict([[2, 9, 6]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
