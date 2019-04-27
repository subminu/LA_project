# LA_project
 LA는 Linear Algebra(선형대수학)의 줄임말로서 프로젝트를 진행하면서 선형대수학의 개념을 이용하여 해당 
개념을 이해하는데 초점을 둔 프로젝트이다. 

## [PROJECT NAME] Analysis on Word Vectors in word which contain connotaion meaning by making a simple model

### 1. Purpose of prject
단어의 함축적 의미를 긍정 또는 부정으로 분류하는 간단한 모델을 만들어 본다.

### 2. How to make the model
*Word2vec*이라는 Python 라이브러리를 이용하도록 한다. *Word2vec*은 단어들을 임베딩(embedding)
하여 단어들을 분석할 수 있도록 도와준다. 쉽게 말하면 *Word2vec*은 단어들을 벡터화 시켜준다. 감정적인
의미를 잘 나타내는(긍정과 부정이 명확한, 극단적인) text를 학습 데이터로 선정한다. 이에 대한 선행 연구가
많이 있다. 그렇기 때문에 구글에 sentiment analysis with Word2vec를 치면 정제된 데이터를 쉽게 구할 수 있다.
해당 프로젝트는 http://ai.stanford.edu/~amaas/data/sentiment/ 에서 약 25000개의 극단적인 영화 리뷰들를 
사용하였다. 영화 평론과 함께 평점이 1에서 10점까지 있다. 여기서 5점 보다 적은 점수를 받으면 negative, 
5점 보다 높으면 positive한 문장이라 하고 학습시켜 model을 만든다.

### 3. How to measure the model
약 25000개의 리뷰중 랜덤으로 12500개의 리뷰로만 학습한 뒤 나머지 12500개의 리뷰를 가지고 test를 진행한다.
모든 리뷰에는 평점과 문장의 성향(positive or negative)이 정해져 있기 때문에 test용 리뷰를 해당 모델에 넣어서 나온 
결과 값이 맞는지 확인하여 정확도를 측정한다.