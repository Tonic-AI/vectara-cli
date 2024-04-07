# ./helptexts/helptext.py

def print_create_corpus_advanced_help():
    help_text = """
Usage: vectara create-corpus-advanced <name> <description> [options]

Arguments:
    <name>         The name of the corpus. This should be a unique name that describes the corpus.
    <description>  A brief description of what the corpus is about.

Options:
    --custom_dimensions JSON_STRING  Optional. A JSON string representing custom dimensions for the corpus.
    --filter_attributes JSON_STRING  Optional. A JSON string representing attributes used for filtering documents within the corpus.
    --public BOOLEAN                 Optional. A boolean flag indicating whether the corpus should be public (true) or private (false). Default is false.
    --encoder_id INT                 Optional. Encoder ID, default is 1.
    --metadata_max_bytes INT         Optional. Maximum metadata bytes, default is 10000.
    --swap_qenc BOOLEAN              Optional. Swap query encoder, default is False.
    --swap_ienc BOOLEAN              Optional. Swap index encoder, default is False.
    --textless BOOLEAN               Optional. If the corpus is textless, default is False.
    --encrypted BOOLEAN              Optional. If the corpus is encrypted, default is True.

Examples of usage:
    vectara create-corpus-advanced "My Corpus" "A corpus containing documents on topic XYZ"
    vectara create-corpus-advanced "Research Papers" "Corpus for academic research papers" --custom_dimensions '{"dimension1": "value1", "dimension2": "value2"}' --filter_attributes '{"author": "John Doe"}'
    vectara create-corpus-advanced "Public Data" "A corpus of public datasets" --public true
"""
    print(help_text)

def print_create_corpus_help():
    help_text = """
Usage: vectara create-corpus <corpus_id> <name> <description> [options]

Arguments:
    <corpus_id>    The unique identifier for the corpus. Must be an integer.
    <name>         The name of the corpus. This should be a unique name that describes the corpus.
    <description>  A brief description of what the corpus is about.

Options:
    --custom_dimensions JSON_STRING  Optional. A JSON string representing custom dimensions for the corpus. 
                                     Custom dimensions allow you to add additional metadata that can be used for 
                                     filtering and querying. Example: '{"dimension1": "value1", "dimension2": "value2"}'
    --filter_attributes JSON_STRING  Optional. A JSON string representing attributes used for filtering documents 
                                     within the corpus. Example: '{"attribute1": "value1", "attribute2": "value2"}'
    --public BOOLEAN                 Optional. A boolean flag indicating whether the corpus should be public 
                                     (true) or private (false). Default is false.

Examples of usage:
    Create a basic corpus:
        vectara create-corpus 123 "My Corpus" "A corpus containing documents on topic XYZ"

    Create a corpus with custom dimensions and filter attributes:
        vectara create-corpus 456 "Research Papers" "Corpus for academic research papers" --custom_dimensions '{"subject": "Computer Science", "year": "2024"}' --filter_attributes '{"author": "John Doe"}'

    Create a public corpus:
        vectara create-corpus 789 "Public Data" "A corpus of public datasets" --public true

Note:
    - Ensure that the JSON strings for --custom_dimensions and --filter_attributes are properly formatted. Incorrect JSON format will result in an error.
    - The --public option is a simple flag. If you want the corpus to be public, include '--public true' in your command. The default behavior is to create a private corpus if the flag is not specified.
"""
    print(help_text)


def print_index_document_help():

    help_text = """
Usage: vectara index-document corpus_id document_id title metadata_json section_text

Arguments:
- corpus_id: The ID of the corpus where the document will be indexed. (integer)
- document_id: A unique identifier for the document. (string)
- title: The title of the document. (string)
- metadata_json: A JSON string containing metadata for the document. Ensure proper escaping. (string)
- section_text: The main content of the document. (string)

Example:
vectara index-document 123 001 "My Document Title" "{\\"author\\":\\"John Doe\\",\\"year\\":2022}" "This is the main content of the document."

This command indexes a document with the specified title, metadata, and content into the corpus with ID 123.
"""
    print(help_text)