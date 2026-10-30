
import gradio as gr
import os

from summarizer import summarize_website


SAMPLES = {
    "🚀 Startup site": "https://example.com/",
    "📰 News article": "https://www.bbc.com/news",
    "✍️ Personal blog": "https://paulgraham.com/articles.html",
}


CSS = """
.gradio-container {
    max-width: 1500px !important;
    margin: auto !important;
    background: #faf5ed !important;
    font-family: Arial, sans-serif !important;
}

#top-bar {
    height: 12px;
    background: linear-gradient(90deg, #ff8500, #ff5738);
    margin-bottom: 0;
}

#main-panel {
    border: 1px solid #eadaca;
    border-radius: 0 0 22px 22px;
    overflow: hidden;
    box-shadow: 0 7px 0 #e4d9cd;
    background: white;
}

#input-panel {
    background: #fcf7ef;
    padding: 26px;
}

#output-panel {
    background: white;
    padding: 26px;
}

#sample-buttons button {
    border-radius: 16px !important;
    font-weight: 600 !important;
    min-height: 48px;
}

#website-url input {
    background: #fcf7ef !important;
    border: 2px solid #eadaca !important;
    border-radius: 14px !important;
    min-height: 48px;
    font-size: 16px !important;
}

#personality-buttons label {
    border-radius: 16px !important;
    font-weight: 600 !important;
}

#summary-output {
    border: 1px solid #eadaca !important;
    border-radius: 18px !important;
    background: #f7ede0 !important;
    min-height: 300px !important;
    padding: 18px !important;
}

#summarize-button {
    background: #ff5738 !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    font-size: 19px !important;
    font-weight: 700 !important;
    min-height: 62px !important;
}

#summarize-button:hover {
    background: #ed482b !important;
}
"""


def run_summarizer(url, personality):
    """Call the summarization layer and display its result."""

    if not url or not url.strip():
        raise gr.Error("Please enter a website URL.")

    print(f"[APP] Summarizing: {url}", flush=True)

    try:
        summary = summarize_website(url.strip(), personality)

        if not summary or not summary.strip():
            raise gr.Error("The summarizer returned an empty response.")

        return summary

    except gr.Error:
        raise

    except Exception as exc:
        print(f"[APP ERROR] {exc}", flush=True)
        raise gr.Error(str(exc)) from exc


with gr.Blocks(
    title="AI Website Summarizer",
) as app:

    gr.HTML('<div id="top-bar"></div>')

    with gr.Row(equal_height=True, elem_id="main-panel"):

        with gr.Column(scale=1, elem_id="input-panel"):

            gr.Markdown("### Pick a sample website")

            with gr.Row(elem_id="sample-buttons"):
                startup_btn = gr.Button("🚀 Startup site")
                news_btn = gr.Button("📰 News article")
                blog_btn = gr.Button("✍️ Personal blog")

            gr.Markdown("### ...or enter any website URL")

            website_url = gr.Textbox(
                placeholder="https://example.com/article",
                label="Website URL",
                show_label=False,
                lines=1,
                elem_id="website-url",
            )

            gr.Markdown("### Personality (the system prompt)")

            personality = gr.Radio(
                choices=[
                    "Friendly",
                    "Snarky",
                    "Explain like I’m 5",
                    "Professional",
                ],
                value="Friendly",
                label=None,
                elem_id="personality-buttons",
            )

            summarize_btn = gr.Button(
                "✨ Summarize",
                variant="primary",
                elem_id="summarize-button",
            )

        with gr.Column(scale=1, elem_id="output-panel"):

            gr.Markdown("### Summary")

            summary_output = gr.Markdown(
                value="_Your summary will appear here..._",
                elem_id="summary-output",
            )

    startup_btn.click(
        fn=lambda: SAMPLES["🚀 Startup site"],
        inputs=[],
        outputs=website_url,
    )

    news_btn.click(
        fn=lambda: SAMPLES["📰 News article"],
        inputs=[],
        outputs=website_url,
    )

    blog_btn.click(
        fn=lambda: SAMPLES["✍️ Personal blog"],
        inputs=[],
        outputs=website_url,
    )

    summarize_btn.click(
        fn=run_summarizer,
        inputs=[website_url, personality],
        outputs=summary_output,
        show_progress="full",
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    app.launch(
        server_name="0.0.0.0",
        server_port=port,
        theme=gr.themes.Soft(
            primary_hue="orange",
            secondary_hue="orange",
            neutral_hue="stone",
        ),
        css=CSS,
    )

