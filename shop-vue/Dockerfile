FROM node:17.9.0

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install

COPY . /app

# start app
CMD npm run serve
#--host 0.0.0.0