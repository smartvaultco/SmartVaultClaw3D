// PM2 Ecosystem Config — Smart Vault Co.
// Run: pm2 start ecosystem.config.js
// This keeps all bots running 24/7 and restarts them if they crash

module.exports = {
  apps: [
    {
      name: 'smart-vault-gateway',
      script: 'index.js',           // OpenClaw gateway entry point (from Claw3D repo)
      cwd: './',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '500M',
      env: {
        NODE_ENV: 'production',
        OPENCLAW_CONFIG: './openclaw.json'
      },
      error_file: './logs/gateway-error.log',
      out_file: './logs/gateway-out.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss',
      restart_delay: 5000,          // Wait 5s before restart on crash
      max_restarts: 10,             // Stop trying after 10 crashes in a row
      min_uptime: '10s'             // Must run 10s to count as successful start
    },

    {
      name: 'smart-vault-scheduler',
      script: 'scheduler.js',       // Cron runner for scheduled bot tasks
      cwd: './',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '200M',
      error_file: './logs/scheduler-error.log',
      out_file: './logs/scheduler-out.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss'
    }
  ]
}
