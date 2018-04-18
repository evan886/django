BEGIN TRANSACTION;
CREATE TABLE "mysite_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "price" integer unsigned NOT NULL, "pmodel_id" integer NOT NULL REFERENCES "mysite_pmodel" ("id"), "nickname" varchar(15) NOT NULL, "year" integer unsigned NOT NULL, "description" text NOT NULL);
INSERT INTO `mysite_product` VALUES (1,500,6,'S3零件機便宜賣',2010,'功能正常，但是螢幕摔裂了，十分可惜。');
INSERT INTO `mysite_product` VALUES (2,1000,3,'4G不錯用備用機',2015,'暫無說明');
INSERT INTO `mysite_product` VALUES (3,100,4,'古董二手機三星雙卡機',2013,'功能正常，便宜賣');
INSERT INTO `mysite_product` VALUES (4,150,1,'Nokia舊機俗俗賣',2010,'功能均正常，可當備用機使用。
支援3G SIM小卡');
INSERT INTO `mysite_product` VALUES (5,2500,5,'SONY TX白色舊機',2013,'老旗艦機，但功能正常，而且有6成新的保護殻');
CREATE INDEX "mysite_product_6e1be4b4" ON "mysite_product" ("pmodel_id");
CREATE INDEX "mysite_pphoto_9bea82de" ON "mysite_pphoto" ("product_id");
CREATE INDEX "mysite_pmodel_8e8bc641" ON "mysite_pmodel" ("maker_id");
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
COMMIT;
