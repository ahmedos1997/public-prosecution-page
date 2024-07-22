# Generated by Django 5.0.3 on 2024-03-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='complainant_nationality',
            field=models.CharField(choices=[('AW', 'آروبا'), ('AZ', 'أذربيجان'), ('AM', 'أرمينيا'), ('ES', 'أسبانيا'), ('AU', 'أستراليا'), ('AF', 'أفغانستان'), ('AL', 'ألبانيا'), ('DE', 'ألمانيا'), ('AG', 'أنتيجوا وبربودا'), ('AO', 'أنجولا'), ('AI', 'أنجويلا'), ('AD', 'أندورا'), ('UY', 'أورجواي'), ('UZ', 'أوزبكستان'), ('UG', 'أوغندا'), ('UA', 'أوكرانيا'), ('IE', 'أيرلندا'), ('IS', 'أيسلندا'), ('ER', 'إريتريا'), ('IL', 'إسرائيل'), ('IR', 'إيران'), ('SZ', 'إيسواتيني'), ('IT', 'إيطاليا'), ('ET', 'اثيوبيا'), ('EE', 'استونيا'), ('AR', 'الأرجنتين'), ('JO', 'الأردن'), ('AE', 'الإمارات العربية المتحدة'), ('EC', 'الاكوادور'), ('BS', 'الباهاما'), ('BH', 'البحرين'), ('BR', 'البرازيل'), ('PT', 'البرتغال'), ('BA', 'البوسنة والهرسك'), ('GA', 'الجابون'), ('ME', 'الجبل الأسود'), ('DZ', 'الجزائر'), ('BQ', 'الجزر الكاريبية الهولندية'), ('DK', 'الدنمارك'), ('SA', 'السعودية (المملكة العربية)'), ('SV', 'السلفادور'), ('SN', 'السنغال'), ('SD', 'السودان'), ('SE', 'السويد'), ('EH', 'الصحراء الغربية'), ('SO', 'الصومال'), ('CN', 'الصين'), ('IQ', 'العراق'), ('PH', 'الفيلبين'), ('AQ', 'القطب الجنوبي'), ('CM', 'الكاميرون'), ('VA', 'الكرسي الرسولي'), ('CG', 'الكونغو'), ('KW', 'الكويت'), ('HU', 'المجر'), ('IO', 'المحيط الهندي البريطاني'), ('MA', 'المغرب'), ('TF', 'المقاطعات الجنوبية الفرنسية'), ('MX', 'المكسيك'), ('GB', 'المملكة المتحدة'), ('NO', 'النرويج'), ('AT', 'النمسا'), ('NE', 'النيجر'), ('IN', 'الهند'), ('US', 'الولايات المتحدة الأمريكية'), ('JP', 'اليابان'), ('YE', 'اليمن'), ('GR', 'اليونان'), ('ID', 'اندونيسيا'), ('PG', 'بابوا غينيا الجديدة'), ('PY', 'باراجواي'), ('PK', 'باكستان'), ('PW', 'بالاو'), ('BW', 'بتسوانا'), ('PN', 'بتكايرن'), ('BB', 'بربادوس'), ('BM', 'برمودا'), ('BN', 'بروناي'), ('BE', 'بلجيكا'), ('BG', 'بلغاريا'), ('BZ', 'بليز'), ('BD', 'بنجلاديش'), ('PA', 'بنما'), ('BJ', 'بنين'), ('BT', 'بوتان'), ('PR', 'بورتوريكو'), ('BF', 'بوركينا فاسو'), ('BI', 'بوروندي'), ('PL', 'بولندا'), ('BO', 'بوليفيا'), ('PF', 'بولينيزيا الفرنسية'), ('PE', 'بيرو'), ('TZ', 'تانزانيا'), ('TH', 'تايلند'), ('TW', 'تايوان'), ('TM', 'تركمانستان'), ('TR', 'تركيا'), ('TT', 'ترينيداد وتوباغو'), ('TD', 'تشاد'), ('CZ', 'تشيكيا'), ('TG', 'توجو'), ('TV', 'توفالو'), ('TK', 'توكيلو'), ('TO', 'تونجا'), ('TN', 'تونس'), ('TL', 'تيمور الشرقية'), ('JM', 'جامايكا'), ('GI', 'جبل طارق'), ('GD', 'جرينادا'), ('GL', 'جرينلاند'), ('AX', 'جزر آلاند'), ('TC', 'جزر الترك وجايكوس'), ('VG', 'جزر العذراء (البريطانية)'), ('VI', 'جزر العذراء (الولايات المتحدة)'), ('KM', 'جزر القمر'), ('KY', 'جزر الكايمن'), ('MH', 'جزر المارشال'), ('MV', 'جزر الملديف'), ('UM', 'جزر الولايات المتحدة البعيدة الصغيرة'), ('SB', 'جزر سليمان'), ('FO', 'جزر فارو'), ('FK', 'جزر فوكلاند (مالفيناس)'), ('CK', 'جزر كوك'), ('CC', 'جزر كوكس'), ('MP', 'جزر ماريانا الشمالية'), ('WF', 'جزر والس وفوتونا'), ('CX', 'جزيرة الكريسماس'), ('BV', 'جزيرة بوفيه'), ('IM', 'جزيرة مان'), ('NF', 'جزيرة نورفوك'), ('HM', 'جزيرة هيرد وماكدونالد'), ('CF', 'جمهورية افريقيا الوسطى'), ('DO', 'جمهورية الدومينيك'), ('CD', 'جمهورية الكونغو الديمقراطية'), ('ZA', 'جنوب افريقيا (الجمهورية)'), ('SS', 'جنوب السودان'), ('GT', 'جواتيمالا'), ('GP', 'جوادلوب'), ('GU', 'جوام'), ('GE', 'جورجيا'), ('GS', 'جورجيا الجنوبية وجزر ساندويتش الجنوبية'), ('DJ', 'جيبوتي'), ('JE', 'جيرسي'), ('GG', 'جيرنزي'), ('DM', 'دومينيكا'), ('RW', 'رواندا'), ('RU', 'روسيا'), ('BY', 'روسيا البيضاء'), ('RO', 'رومانيا'), ('RE', 'روينيون'), ('ZM', 'زامبيا'), ('ZW', 'زيمبابوي'), ('CI', 'ساحل العاج'), ('WS', 'ساموا'), ('AS', 'ساموا الأمريكية'), ('SM', 'سان مارينو'), ('BL', 'سانت بارتيليمي'), ('PM', 'سانت بيير وميكولون'), ('VC', 'سانت فنسنت وغرنادين'), ('KN', 'سانت كيتس ونيفيس'), ('LC', 'سانت لوسيا'), ('MF', 'سانت مارتن (الجزء الفرنسي)'), ('SX', 'سانت مارتن (الجزء الهولندي)'), ('SH', 'سانت هيلنا'), ('ST', 'ساو تومي وبرينسيبي'), ('LK', 'سريلانكا'), ('SJ', 'سفالبارد وجان مايان'), ('SK', 'سلوفاكيا'), ('SI', 'سلوفينيا'), ('SG', 'سنغافورة'), ('SY', 'سوريا'), ('SR', 'سورينام'), ('CH', 'سويسرا'), ('SL', 'سيراليون'), ('SC', 'سيشل'), ('CL', 'شيلي'), ('RS', 'صربيا'), ('TJ', 'طاجكستان'), ('OM', 'عُمان'), ('GM', 'غامبيا'), ('GH', 'غانا'), ('GF', 'غويانا'), ('GY', 'غيانا'), ('GN', 'غينيا'), ('GQ', 'غينيا الاستوائية'), ('GW', 'غينيا بيساو'), ('VU', 'فانواتو'), ('FR', 'فرنسا'), ('PS', 'فلسطين'), ('VE', 'فنزويلا'), ('FI', 'فنلندا'), ('VN', 'فيتنام'), ('FJ', 'فيجي'), ('CY', 'قبرص'), ('KG', 'قرغيزستان'), ('QA', 'قطر'), ('CV', 'كابو فيردي'), ('KZ', 'كازاخستان'), ('NC', 'كاليدونيا الجديدة'), ('HR', 'كرواتيا'), ('KH', 'كمبوديا'), ('CA', 'كندا'), ('CU', 'كوبا'), ('CW', 'كوراساو'), ('KR', 'كوريا الجنوبية'), ('KP', 'كوريا الشمالية'), ('CR', 'كوستاريكا'), ('CO', 'كولومبيا'), ('KI', 'كيريباتي'), ('KE', 'كينيا'), ('LV', 'لاتفيا'), ('LA', 'لاوس'), ('LB', 'لبنان'), ('LU', 'لوكسمبورج'), ('LY', 'ليبيا'), ('LR', 'ليبيريا'), ('LT', 'ليتوانيا'), ('LI', 'ليختنشتاين'), ('LS', 'ليسوتو'), ('MQ', 'مارتينيك'), ('MO', 'ماكاو'), ('MT', 'مالطا'), ('ML', 'مالي'), ('MY', 'ماليزيا'), ('YT', 'مايوت'), ('MG', 'مدغشقر'), ('EG', 'مصر'), ('MK', 'مقدونيا الشمالية'), ('MW', 'ملاوي'), ('MN', 'منغوليا'), ('MR', 'موريتانيا'), ('MU', 'موريشيوس'), ('MZ', 'موزمبيق'), ('MD', 'مولدافيا'), ('MC', 'موناكو'), ('MS', 'مونتسرات'), ('MM', 'ميانمار'), ('FM', 'ميكرونيسيا (الولايات المتحدة)'), ('NA', 'ناميبيا'), ('NR', 'نورو'), ('NP', 'نيبال'), ('NG', 'نيجيريا'), ('NI', 'نيكاراجوا'), ('NZ', 'نيوزيلاندا'), ('NU', 'نيوي'), ('HT', 'هايتي'), ('HN', 'هندوراس'), ('NL', 'هولندا'), ('HK', 'هونج كونج الصينية'), ('', 'Select Country')], max_length=200, null=True),
        ),
    ]
