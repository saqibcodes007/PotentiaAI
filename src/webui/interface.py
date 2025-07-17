# src/webui/interface.py

import gradio as gr

from src.webui.webui_manager import WebuiManager
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab

theme_map = {
    "Default": gr.themes.Default(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass(),
    "Origin": gr.themes.Origin(),
    "Citrus": gr.themes.Citrus(),
    "Ocean": gr.themes.Ocean(),
    "Base": gr.themes.Base()
}


# +++ PASTE THIS NEW FUNCTION IN ITS PLACE +++

def create_ui(theme_name="Ocean"):
    # +++ PASTE THIS NEW CSS BLOCK IN ITS PLACE +++
    css = """
    .gradio-container {
        width: 70vw !important;
        max-width: 960px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        background-color: #121212 !important;
    }

    footer {
        display: none !important;
    }

    /* Fix 1: Ensures the header row is centered */
    .header-container {
        display: flex;
        justify-content: center !important; /* This is key for horizontal alignment */
        align-items: center;
        gap: 1.5rem;
        margin-bottom: 2rem;
        width: 100%; /* Forces the container to span the full width */
    }

    /* This is your logo code, it is perfect and unchanged */
    #logo {
        max-width: 80px !important;
        min-width: 80px !important;
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
    }
    #logo img {
        width: 80px !important;
        object-fit: contain;
    }

    .title-container {
        text-align: center;
        overflow: hidden;
    }

    /* Fix 2: Reduces title size and keeps the correct font/color */
    #title-text h1 {
        font-family: 'Poppins', sans-serif !important;
        font-size: 2.8rem !important; /* Reduced from 4rem */
        font-weight: 700 !important;
        line-height: 1.1 !important;
        background: linear-gradient(90deg, #00aaff, #e000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 10px rgba(0, 170, 255, 0.5), 0 0 20px rgba(224, 0, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0 !important;
        padding: 0 !important;
    }

    #subtitle h3 {
        font-family: 'Poppins', sans-serif !important;
        font-size: 1.2rem !important;
        font-weight: 400 !important;
        color: #ccc !important;
        letter-spacing: 0.5px;
        margin: 0 !important;
        padding: 0 !important;
    }

    .tab-header-text { text-align: center; }
    .theme-section { margin-bottom: 10px; padding: 15px; border-radius: 10px; }
    .footer { padding: 2rem 0; margin-top: 3rem; font-size: 0.9rem; text-align: center; color: #666; border-top: 1px solid #333; }
    """

    head = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    """

    js_func = """
    function refresh() {
        const url = new URL(window.location);
        if (url.searchParams.get('__theme') !== 'dark') {
            url.searchParams.set('__theme', 'dark');
            window.location.href = url.href;
        }
    }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
            title="Potentia AI", theme=theme_map[theme_name], css=css, js=js_func, head=head,
    ) as demo:
        with gr.Row(elem_id="header-container"):
            gr.Image(value="src/webui/owl-logo.png", show_label=False, interactive=False, show_download_button=False, elem_id="logo")
            with gr.Column(elem_id="title-container", scale=1, min_width=0):
                gr.Markdown("# Potentia AI", elem_id="title-text")
                gr.Markdown("### By Saqib Sherwani", elem_id="subtitle")

        with gr.Tabs() as tabs:
            with gr.TabItem("⚙️ Agent Settings"):
                create_agent_settings_tab(ui_manager)
            with gr.TabItem("🌐 Browser Settings"):
                create_browser_settings_tab(ui_manager)
            with gr.TabItem("🤖 Run Agent"):
                create_browser_use_agent_tab(ui_manager)
            with gr.TabItem("🎁 Agent Marketplace"):
                gr.Markdown("### Agents built on Browser-Use", elem_classes=["tab-header-text"])
                with gr.Tabs():
                    with gr.TabItem("Deep Research"):
                        create_deep_research_agent_tab(ui_manager)
            with gr.TabItem("📁 Load & Save Config"):
                create_load_save_config_tab(ui_manager)

        gr.Markdown(
            """
            ---
            <div style='padding:2rem 0;margin-top:3rem;font-size:0.9rem;text-align:center;color:#666;border-top:1px solid #333;'>
                Potentia AI © 2025 | Panacea Smart Solutions | Developed by Saqib Sherwani | All rights reserved.
            </div>
            """
        )
    return demo

# def create_ui(webui_manager: WebuiManager) -> gr.Blocks:
#     """Creates the main Gradio UI layout and registers all event handlers."""
#     # Define themes
#     theme_map = {
#         "Default": gr.themes.Default(),
#         "Soft": gr.themes.Soft(),
#         "Monochrome": gr.themes.Monochrome(),
#         "Glass": gr.themes.Glass(),
#     }
    
#     # Correctly get the theme name from the manager before creating the Blocks
#     theme_name = webui_manager.get_setting("theme_name", "Default")
#     selected_theme = theme_map.get(theme_name, theme_map["Default"]) # Safely get the theme

#     # Load JS and CSS
#     css, js_func, head = load_assets()

#     with gr.Blocks(
#         title="Potentia AI", theme=selected_theme, css=css, js=js_func, head=head
#     ) as demo:
#         # Store components for easy access
#         components = {}

#         # Main UI structure
#         with gr.Row():
#             with gr.Column(scale=1):
#                 # Left panel for settings and controls
#                 gr.Markdown("## ⚙️ Settings & Controls")
#                 create_load_save_config_tab(webui_manager, components)
#                 create_agent_settings_tab(webui_manager, components)
#                 create_browser_settings_tab(webui_manager, components)

#             with gr.Column(scale=2):
#                 # Right panel for agent interaction
#                 gr.Markdown("## 🤖 Agent Interaction")
#                 create_browser_use_agent_tab(webui_manager, components)

#         # --- Event Handlers ---
#         # Link UI components to their backend functions
#         register_event_handlers(webui_manager, components)

#         # Make components accessible globally
#         webui_manager.set_all_components(components)

#     return demo