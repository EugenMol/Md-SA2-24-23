# этап устновки (install stage)
FROM node:lts-alpine as installer
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# этап сборки (build stage)
FROM installer as build
RUN npm run build

# этап production (production-stage)
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]