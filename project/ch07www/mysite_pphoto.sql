BEGIN TRANSACTION;
CREATE TABLE "mysite_pphoto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "url" varchar(200) NOT NULL, "product_id" integer NOT NULL REFERENCES "mysite_product" ("id"), "description" varchar(20) NOT NULL);
INSERT INTO `mysite_pphoto` VALUES (1,'http://i.imgur.com/zamweOK.jpg',1,'S3正面照片');
INSERT INTO `mysite_pphoto` VALUES (2,'http://i.imgur.com/vg34aYM.jpg',1,'S3背面照片');
INSERT INTO `mysite_pphoto` VALUES (3,'http://i.imgur.com/qDbAzoe.jpg',4,'Nokia 5800正面照');
INSERT INTO `mysite_pphoto` VALUES (4,'http://i.imgur.com/9rFsffi.jpg',4,'Nokia 5800背面照');
INSERT INTO `mysite_pphoto` VALUES (5,'http://i.imgur.com/OEOTvmy.jpg',5,'SONY TX正面照');
INSERT INTO `mysite_pphoto` VALUES (6,'http://i.imgur.com/uX2Kmpy.jpg',5,'SONY TX背面照(含保護殻）');
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