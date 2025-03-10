FROM node:18
WORKDIR /app
COPY ../../package.json ../../pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install
COPY . .
RUN pnpm nx build next
EXPOSE 4200
CMD ["pnpm", "nx", "serve", "next"]