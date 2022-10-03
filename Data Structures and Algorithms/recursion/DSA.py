{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "79072756",
   "metadata": {},
   "outputs": [],
   "source": [
    "def reverse(string):\n",
    "    string = string[::-1]\n",
    "    return string\n",
    "\n",
    "def reverseTwo(string):\n",
    "    str = \"\"\n",
    "    for i in string:\n",
    "        str = i + str\n",
    "    return str\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4169ff2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial is:  120\n"
     ]
    }
   ],
   "source": [
    "# Factorial using recursion\n",
    "def myfact(n):\n",
    "    if n==1:\n",
    "        return n\n",
    "    else:\n",
    "        return n * myfact(n-1)\n",
    "\n",
    "num = 5\n",
    "if num < 0:\n",
    "    print(\"No negative no\")\n",
    "elif num == 0:\n",
    "    print(\"Factorial is: 1\")\n",
    "else:\n",
    "    print(\"Factorial is: \", myfact(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f52132f5",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mCanceled future for execute_request message before replies were done"
     ]
    },
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mThe Kernel crashed while executing code in the the current cell or a previous cell. Please review the code in the cell(s) to identify a possible cause of the failure. Click <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": [
    "# Fibonacci Series\n",
    "def fib(n):\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    else:\n",
    "        return (fib(n-1) + fib(n+2))\n",
    "\n",
    "count = 6\n",
    "\n",
    "if count <= 0:\n",
    "    print(\"Please enter value more than 2\")\n",
    "else:\n",
    "    for i in range(count):\n",
    "        print(fib(i), end=\" \")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8.4 64-bit",
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
   "version": "3.8.4"
  },
  "vscode": {
   "interpreter": {
    "hash": "9650cb4e16cdd4a8e8e2d128bf38d875813998db22a3c986335f89e0cb4d7bb2"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
