from collections import ChainMap 

# ChainMap combines multiple dictionaries into a single, accessible unit.

# 1. Initializing dictionaries
default_settings = {'theme': 'dark', 'font_size': 12, 'show_sidebar': True}
user_settings = {'font_size': 16, 'show_sidebar': False}
session_settings = {'theme': 'light'}

# 2. Defining the ChainMap (Order matters: earlier dictionaries take precedence)
settings_chain = ChainMap(session_settings, user_settings, default_settings)
print(f"2. Settings ChainMap: {settings_chain}")

# 3. Accessing Values
# Accessing 'theme' checks session_settings first, then user_settings, then default_settings.
print(f"3. Current 'theme' (from session_settings): {settings_chain['theme']}") 
print(f"   Current 'font_size' (from user_settings): {settings_chain['font_size']}")
print(f"   Current 'show_sidebar' (from user_settings): {settings_chain['show_sidebar']}")

# 4. Adding a new dictionary (using new_child)
# The new dictionary is added at the beginning, giving it the highest precedence.
runtime_override = {'show_sidebar': True, 'logging_level': 'DEBUG'}
final_settings = settings_chain.new_child(runtime_override)

print(f"\n4. Final Settings ChainMap (with runtime override):")
print(final_settings)
print(f"   New 'show_sidebar' (from runtime_override): {final_settings['show_sidebar']}")
print(f"   New 'logging_level' (unique key): {final_settings['logging_level']}")