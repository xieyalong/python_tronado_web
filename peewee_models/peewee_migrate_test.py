
from peewee_models import  models
from peewee_migrate import Router

router = Router(models.db)

# 创建迁移
router.create(auto=models)
# 运行迁移/迁移
# router.run('xyl_user')

# 运行所有未应用的迁移
router.run()

models.db.close()