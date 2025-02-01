# 1. Node.js asosiy image (LTS versiyasi)
FROM node:18-alpine

# 2. Ishlash papkasi
WORKDIR /app

# 3. Faqat package.json va package-lock.json nusxalash
COPY package*.json ./

# 4. Qaramliklarni o'rnatish
RUN npm install

# 5. Barcha fayllarni nusxalash
COPY . .

EXPOSE 3000

# 8. React ilovasini ishga tushirish (development mode)
CMD ["npm", "start"]

