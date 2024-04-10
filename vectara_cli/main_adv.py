# ./main_adv.py

import argparse
import sys
from vectara_cli.commands import (
    advanced_query_main,
    index_text_adv,
    # index_document,
    create_corpus_adv,
    delete_corpus_adv
    # span_text,
    # span_enhance_folder,
    # upload_document,
    # upload_enriched_text,
    # nerdspan_upsert_folder,
    # rebel_upsert_folder,
    # advanced_query,
    # index_text,
)
from vectara_cli.utils.create_ui import create_ui
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.utils.utils import get_vectara_client, set_api_keys as set_api_keys_main
from vectara_cli.helptexts.help_text import main_help_text
from vectara_cli.commands.create_corpus_adv import setup_arg_parser as setup_create_corpus_adv_parser
from vectara_cli.commands.delete_corpus_adv import setup_arg_parser as setup_delete_corpus_adv_parser

def set_api_keys(args):
    set_api_keys_main(args.customer_id, args.api_key)

def delete_corpus_adv(args):
    vectara_client = get_vectara_client()
    from vectara_cli.commands.delete_corpus_adv import main as delete_corpus_main
    delete_corpus_main(args, vectara_client)

def command_func_wrapper(command_func, vectara_client):
    def wrapper(args):
        extra_args = sys.argv[2:] 
        command_func(extra_args, vectara_client())
    return wrapper

def main():
    parser = argparse.ArgumentParser(description="Vectara CLI Tool")
    subparsers = parser.add_subparsers(dest='command', help='commands')
    setup_delete_corpus_adv_parser(subparsers)
    set_api_keys_main(subparsers)
    setup_create_corpus_adv_parser(subparsers)
    setup_create_corpus_adv_parser(subparsers)
    
    # set_api_keys_parser = subparsers.add_parser('set-api-keys', help='Set the API keys')
    # set_api_keys_parser.add_argument('customer_id', type=str, help='Customer ID')
    # set_api_keys_parser.add_argument('api_key', type=str, help='API Key')
    # set_api_keys_parser.set_defaults(func=set_api_keys)

    commands = {
        "create-ui": create_ui,
        "advanced-query-adv": advanced_query_main,
        "index-document-adv": index_text_adv.main,
        "create-corpus-adv": setup_create_corpus_adv_parser(subparsers)
        # "index-document": index_document.main,
        "delete-corpus": delete_corpus_adv.main,
        # "span-text": span_text.main,
        # "span-enhance-folder": span_enhance_folder.main,
        # "upload-document": upload_document.main,
        # "upload-enriched-text": upload_enriched_text.main,
        # "nerdspan-upsert-folder": nerdspan_upsert_folder.main,
        # "rebel-upsert-folder": rebel_upsert_folder.main,
        # "index-text": index_text.main,
        # "advanced-query": advanced_query.main,

    }

    for command_name, command_func in commands.items():
        command_parser = subparsers.add_parser(command_name, help=f'{command_name} command')
        command_parser.set_defaults(func=command_func_wrapper(command_func))

    args = parser.parse_args()

    if hasattr(args, 'func'):
        if args.command == "set-api-keys":
            args.func(args)
        else:
            try:
                vectara_client = get_vectara_client()
                args.func(args, vectara_client)
            except ValueError as e:
                print(e)
                sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()