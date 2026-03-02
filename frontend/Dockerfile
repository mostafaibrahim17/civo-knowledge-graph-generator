FROM nginx:alpine

# Copy static frontend to nginx public directory
COPY index.html /usr/share/nginx/html/

# Expose port 80 for Civo LoadBalancer
EXPOSE 80

# Simple healthcheck
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget -qO- http://localhost:80/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
