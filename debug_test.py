#!/usr/bin/env python3
"""
سكريبت اختبار لتشخيص خطأ 500
"""

import os
import sys
import traceback

def test_imports():
    """اختبار الاستيرادات"""
    print("🔍 اختبار الاستيرادات...")
    try:
        from flask import Flask
        print("✅ Flask")
    except Exception as e:
        print(f"❌ Flask: {e}")
        return False

    try:
        from flask_restx import Api
        print("✅ Flask-RESTX")
    except Exception as e:
        print(f"❌ Flask-RESTX: {e}")
        return False

    try:
        from flask_limiter import Limiter
        print("✅ Flask-Limiter")
    except Exception as e:
        print(f"❌ Flask-Limiter: {e}")
        return False

    try:
        import redis
        print("✅ Redis")
    except Exception as e:
        print(f"❌ Redis: {e}")
        return False

    try:
        import psutil
        print("✅ Psutil")
    except Exception as e:
        print(f"❌ Psutil: {e}")
        return False

    return True

def test_app_creation():
    """اختبار إنشاء التطبيق"""
    print("\n🔍 اختبار إنشاء التطبيق...")
    try:
        # تعيين متغيرات البيئة للتطوير
        os.environ['FLASK_ENV'] = 'development'

        from app import app
        print("✅ تم إنشاء التطبيق بنجاح")

        # اختبار نقطة نهاية بسيطة
        with app.test_client() as client:
            response = client.get('/api')
            print(f"✅ استجابة API: {response.status_code}")
            print(f"البيانات: {response.get_json()}")

        return True

    except Exception as e:
        print(f"❌ فشل في إنشاء التطبيق: {e}")
        print("تتبع الخطأ:")
        traceback.print_exc()
        return False

def test_specific_endpoints():
    """اختبار نقاط نهاية محددة"""
    print("\n🔍 اختبار نقاط النهاية...")
    try:
        os.environ['FLASK_ENV'] = 'development'
        from app import app

        with app.test_client() as client:
            # اختبار /health
            response = client.get('/health')
            print(f"✅ /health: {response.status_code}")

            # اختبار /stats
            response = client.get('/stats')
            print(f"✅ /stats: {response.status_code}")

            # اختبار /api/docs
            response = client.get('/api/docs')
            print(f"✅ /api/docs: {response.status_code}")

        return True

    except Exception as e:
        print(f"❌ فشل في اختبار نقاط النهاية: {e}")
        traceback.print_exc()
        return False

def main():
    print("🚀 بدء تشخيص خطأ 500 Internal Server Error")
    print("=" * 50)

    # اختبار الاستيرادات
    if not test_imports():
        print("\n❌ فشل في الاستيرادات الأساسية")
        sys.exit(1)

    # اختبار إنشاء التطبيق
    if not test_app_creation():
        print("\n❌ فشل في إنشاء التطبيق")
        sys.exit(1)

    # اختبار نقاط النهاية
    if not test_specific_endpoints():
        print("\n❌ فشل في نقاط النهاية")
        sys.exit(1)

    print("\n✅ جميع الاختبارات نجحت!")
    print("إذا كان هناك خطأ 500، فهو ربما يحدث في:")
    print("1. عملية التحويل (/convert)")
    print("2. تحميل الملفات (/download)")
    print("3. مشاكل في قاعدة البيانات أو Redis")

if __name__ == '__main__':
    main()
