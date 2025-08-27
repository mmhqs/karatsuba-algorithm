# Karatsuba Algorithm
This repo presents a Python implementation of the Karastsuba algorithm.

[1. Who's the guy?](#whos-the-guy)

[2. The math behind the algorithm](#the-math-behind-the-algorithm)

[3. How to run the project in Python 🐍](#how-to-run-the-project-in-python)

[4. Algorithm analyses](#algorithm-analyses)

---

## Who's the guy?
[Anatoli Alexeievitch Karatsuba](https://pt.wikipedia.org/wiki/Anatoli_Alexeievitch_Karatsuba) was a russian mathematician who created a method to multiply two natural numbers, way faster than the traditional multiplication methods. The called Karastsuba algorithm started a new class of divide and conquer algorithms.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/ca479f58-79c6-4e03-8287-50e0196cb080" style="border-radius: 10px" />

## The math behind the algorithm
First of all: the math.

To understand the math behind the algorithm, I did some studying and compiled my research in the [karatsuba-study](docs/karatsuba-study.md) file.

After studying the Karatsuba algorithm a little, I implemented the algorithm in Python. I also **added comments to the code** to make it easier to understand each step of the algorithm.

## How to run the project in Python 🐍
The Karatsuba algorithm, implemented in Python, can be found in [main.py](code/main.py) file. You can download it if you want to run it on your computer.

This guide assumes you already have Python installed on your computer, ok? ✅

### Step 1: open your terminal 🖥️
First, you need to open a command-line interface.

### Step 2: navigate to the correct folder 📂
You must tell the terminal where your `main.py` file is located. You'll use the `cd` (change directory) command for this. Find the path to the folder containing the `main.py` file you downloaded from this repo.

Type cd followed by a space and the path to your folder. Example:

`cd Folder1/Folder2/Folder3/MyProject`

### Step 3: run the file ▶️
Once you are in the correct folder, you can run the Python script. Type python followed by the name of your file. Example:

`python main.py`

Enjoy your multiplications!

## Algorithm analysis
After studying the algorithm and implementing the code in Python, it is time to understand the complexity of the algorithm! You can find the full analysis in the [karatsuba-analysis](docs/karatsuba-analysis.md) file.

<img width="500" alt="image" src="docs/images/complexity.PNG" style="border-radius: 10px" />
