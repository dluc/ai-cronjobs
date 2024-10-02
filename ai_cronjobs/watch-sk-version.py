import os
from langchain.prompts import PromptTemplate
from lib.ai import run_structured_prompt
from lib.files import read_text, store_text
from lib.http import get_text_from_url
from lib.notifications import notify
from pydantic import BaseModel, Field

cfg = {
    "url": "https://www.nuget.org/packages/Microsoft.SemanticKernel.Core",
    "prompt": "Extract Semantic Kernel the version number from this text: {content}",
    "data_file": "watch-sk-version.dat",
    "llm_model": "gpt-4o",
}


class SkDetails(BaseModel):
    setup: str = Field(description="Semantic Kernel information")
    version: str = Field(description="Nuget package version")


def get_version_from_content(content, config) -> SkDetails:
    prompt = PromptTemplate(template=config["prompt"], input_variables=["content"]).format(content=content)

    return run_structured_prompt(prompt, config["llm_model"], SkDetails)


def check_if_version_changed(config):
    content = get_text_from_url(config["url"])
    sk = get_version_from_content(content, config)

    if sk.version is None:
        print("Info not found.")
        return

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), config["data_file"])

    previous_version = read_text(file_path)
    print("Previous version:", previous_version)
    print("Current version:", sk.version)

    if previous_version != sk.version:
        print(f"New Semantic Kernel version: {sk.version}")
        notify(f"New Semantic Kernel version: {sk.version}")
        store_text(file_path, sk.version)
    else:
        print("No change detected.")


# ===================================================================
if __name__ == "__main__":
    check_if_version_changed(cfg)
