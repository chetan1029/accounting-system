#### Stage 1: Build the react application
FROM node:16-alpine as build

WORKDIR /app

COPY . ./
RUN npm install


EXPOSE 3000

CMD [ "npm", "run", "dev" ]
