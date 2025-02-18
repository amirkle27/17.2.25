
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

from q3_a import Q3A
from q3_b import Q3B
from q3_c import Q3C
from question_1 import Question1
from question_2 import Question2




if __name__ == "__main__":
    q1 = Question1()
    q2  =Question2()
    q3a = Q3A()
    q3b = Q3B()
    q3c = Q3C()


    print(q1.question_1())
    print()
    print(q2.question_2())
    print()
    print(q3a.q3_a())
    print()
    print(q3b.q3_b())
    print()
    print(q3c.q3_c())

