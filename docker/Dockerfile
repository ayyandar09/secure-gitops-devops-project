# ---- Base image ----
FROM python:3.11-slim

# ---- Security: create non-root user ----
RUN useradd -m appuser

# ---- Set working directory ----
WORKDIR /app

# ---- Copy only required files ----
COPY app/requirements.txt .

# ---- Install dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application source ----
COPY app/src ./src

# ---- Change ownership ----
RUN chown -R appuser:appuser /app

# ---- Switch to non-root user ----
USER appuser

# ---- Expose application port ----
EXPOSE 5000

# ---- Run the application ----
CMD ["python", "src/main.py"]

