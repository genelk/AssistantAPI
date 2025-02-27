"""
Example script demonstrating document summarization functionality.
"""
import os
import sys
import argparse
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src.document_loader import DocumentLoader
from src.models.model_factory import ModelFactory
from src.summarizer import Summarizer

def main():
    """Run the summary generation example."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Generate summaries for a document")
    parser.add_argument("file_path", help="Path to the document file")
    parser.add_argument("--length", choices=["very_short", "short", "medium",
