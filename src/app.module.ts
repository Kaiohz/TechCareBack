import { Module } from '@nestjs/common';
import { HealthController } from './controllers/health.controller.js';
import { HealthService } from './services/health.service.js';
import { PostgreInsertController } from './controllers/postgre.controller.js';
import { PostgreService } from './services/postgre.service.js';

@Module({
  imports: [],
  controllers: [HealthController, PostgreInsertController],
  providers: [HealthService, PostgreService],
})
// eslint-disable-next-line prettier/prettier
export class AppModule { }
