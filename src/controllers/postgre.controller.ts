import { Controller, Post } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { PostgreService } from '../services/postgre.service.js';

@ApiTags('postgre')
@Controller('insert')
export class PostgreInsertController {
  // eslint-disable-next-line prettier/prettier
    constructor(private readonly postgreService: PostgreService) { }

  @Post('supplier')
  async getHealth(): Promise<string> {
    return await this.postgreService.saveSupplier();
  }
}
