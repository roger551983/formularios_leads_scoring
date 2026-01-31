FROM node:20-alpine AS build

WORKDIR /app

# Copiamos dependencias primero (mejor cache)
COPY package*.json ./
RUN npm install

# Copiamos el resto del proyecto
COPY . .

# Construimos Angular
RUN npm run build


# ============================
# Etapa 2: Nginx
# ============================
FROM nginx:alpine

# Eliminamos configuración por defecto
RUN rm /etc/nginx/conf.d/default.conf

# Copiamos configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiamos el build de Angular
COPY --from=build /app/dist/formularios_scoring/browser /usr/share/nginx/html

# Exponemos puerto 80
EXPOSE 80

# Arranque de Nginx
CMD ["nginx", "-g", "daemon off;"]