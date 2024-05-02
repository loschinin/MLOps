# fe/Dockerfile
FROM node:14-alpine as build
WORKDIR /app
COPY fe/package.json fe/package-lock.json ./
RUN npm install
COPY fe/ .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
