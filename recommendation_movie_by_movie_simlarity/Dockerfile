FROM neo4j:4.2.1

ENV NEO4J_HOME="/var/lib/neo4j"   
ENV NEO4J_PASSWD test 
ENV PATH "${NEO4J_HOME}"/bin:$PATH
ENV HOSTNAME bolt://$HOST:7687
EXPOSE 7687 7474 8080

COPY load_data.cql ${NEO4J_HOME}/import/
COPY movie_query.cql .

################## install dependencies and get csv files from website ##########
RUN apt-get update && \
    apt-get install -y wget unzip && \
    mkdir -p example && \
    cd example/ && \
    wget -r --no-check-certificate https://files.grouplens.org/datasets/movielens/ml-latest-small.zip && \
    unzip files.grouplens.org/datasets/movielens/ml-latest-small.zip  && \   
    mv ml-latest-small/*  ${NEO4J_HOME}/import/. && rm -rf files.grouplens.org  ml-latest-small && \
    rm -rf ../example
#
RUN mkdir -p example1 && \
    cd example1/ && \
    wget -r --no-check-certificate https://files.grouplens.org/datasets/movielens/ml-25m.zip && \
    unzip files.grouplens.org/datasets/movielens/ml-25m.zip && \
    mv ml-25m/genome-scores.csv ${NEO4J_HOME}/import/. && \
    rm -rf files.grouplens.org  ml-25m && \
    rm -rf ../example1
#################################################################

#######  python pre-processing data : new csv files  ############
RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 --no-cache-dir install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install numpy scipy pandas datetime scikit-learn 
COPY pre_processing.py . 
RUN cd ${NEO4J_HOME} && python3 pre_processing.py 
##################################################################

################## neo4j load database   #########################
CMD bin/neo4j-admin set-initial-password ${NEO4J_PASSWD} && \
    bin/neo4j start && sleep 10 && \
    if [ -f "${NEO4J_HOME}/import/load_data.cql" ]; then  \
        cat ${NEO4J_HOME}/import/load_data.cql  | NEO4J_USERNAME=neo4j NEO4J_PASSWORD=${NEO4J_PASSWD} bin/cypher-shell --fail-fast && rm ${NEO4J_HOME}/import/load_data.cql ; \
        echo "data load finished ..."; \
    fi && \
   /bin/bash
##################################################################

