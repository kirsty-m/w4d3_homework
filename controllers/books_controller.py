from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint= Blueprint("books", __name__)



@books_blueprint.route("/")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)


@books_blueprint.route("/books/new")
def new_books():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)