#!/usr/bin/env python3
"""
Check configuration and verify all paths are correctly set
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def check_config():
    """Verify all configuration settings"""
    
    # Load environment variables
    env_path = Path(__file__).parent.parent / '.env'
    
    print("=" * 80)
    print("Configuration Check")
    print("=" * 80)
    print()
    
    # Check .env file existence
    if not env_path.exists():
        print(f"❌ .env file not found at: {env_path}")
        print(f"   Please copy env.example to .env and configure it:")
        print(f"   cp {Path(__file__).parent}/env.example {env_path}")
        return False
    
    print(f"✅ .env file found: {env_path}")
    load_dotenv(env_path)
    print()
    
    all_ok = True
    
    # Check repository paths
    print("Repository Paths:")
    print("-" * 80)
    
    comfyui_path = os.getenv('COMFYUI_PATH')
    if comfyui_path:
        path = Path(comfyui_path)
        if path.exists():
            print(f"✅ COMFYUI_PATH: {path}")
            # Check for key files
            if (path / "nodes.py").exists():
                print(f"   ✓ Found nodes.py")
            if (path / "comfy_extras").exists():
                print(f"   ✓ Found comfy_extras/")
        else:
            print(f"❌ COMFYUI_PATH not found: {path}")
            all_ok = False
    else:
        print(f"⚠️  COMFYUI_PATH not set in .env")
        all_ok = False
    
    print()
    
    frontend_path = os.getenv('COMFYUI_FRONTEND_PATH')
    if frontend_path:
        path = Path(frontend_path)
        if path.exists():
            print(f"✅ COMFYUI_FRONTEND_PATH: {path}")
        else:
            print(f"❌ COMFYUI_FRONTEND_PATH not found: {path}")
            all_ok = False
    else:
        print(f"⚠️  COMFYUI_FRONTEND_PATH not set (optional)")
    
    print()
    
    embedded_docs_path = os.getenv('EMBEDDED_DOCS_PATH')
    if embedded_docs_path:
        path = Path(embedded_docs_path)
        if path.exists():
            print(f"✅ EMBEDDED_DOCS_PATH: {path}")
            docs_path = path / "comfyui_embedded_docs" / "docs"
            if docs_path.exists():
                print(f"   ✓ Found docs directory: {docs_path}")
                # Count existing docs
                doc_count = len([d for d in docs_path.iterdir() if d.is_dir()])
                print(f"   ✓ Existing node docs: {doc_count}")
        else:
            print(f"❌ EMBEDDED_DOCS_PATH not found: {path}")
            all_ok = False
    else:
        print(f"⚠️  EMBEDDED_DOCS_PATH not set in .env")
        all_ok = False
    
    print()
    print("API Configuration:")
    print("-" * 80)
    
    # Check API key
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if api_key and api_key != 'your_deepseek_api_key_here':
        print(f"✅ DEEPSEEK_API_KEY: {'*' * 20}{api_key[-4:]}")
    else:
        print(f"❌ DEEPSEEK_API_KEY not configured")
        all_ok = False
    
    # Check API settings
    api_base = os.getenv('API_BASE_URL', 'https://api.deepseek.com')
    api_model = os.getenv('API_MODEL', 'deepseek-chat')
    print(f"✅ API_BASE_URL: {api_base}")
    print(f"✅ API_MODEL: {api_model}")
    
    print()
    print("Batch Settings:")
    print("-" * 80)
    batch_size = os.getenv('BATCH_SIZE', '5')
    max_retries = os.getenv('MAX_RETRIES', '3')
    delay = os.getenv('DELAY_BETWEEN_REQUESTS', '2')
    print(f"✅ BATCH_SIZE: {batch_size}")
    print(f"✅ MAX_RETRIES: {max_retries}")
    print(f"✅ DELAY_BETWEEN_REQUESTS: {delay}s")
    
    print()
    print("=" * 80)
    if all_ok:
        print("✅ All critical configurations are correct!")
        print("   You can now run:")
        print("   python3 scan_missing_nodes.py")
    else:
        print("❌ Some configurations need attention.")
        print("   Please update your .env file.")
    print("=" * 80)
    
    return all_ok

if __name__ == "__main__":
    sys.exit(0 if check_config() else 1)

