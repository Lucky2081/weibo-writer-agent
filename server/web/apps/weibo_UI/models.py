# -*- coding: utf-8 -*-
# Standard library imports.
import datetime
# Related third party imports.
from sqlalchemy.orm import Mapped, mapped_column
# Local application/library specific imports.
from extends import (
    db,
)
from configs import config

cst_tz = config.cst_tz


class weibo_UI_Model(db.Model):
    __tablename__ = 'weibo_UI'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    text: Mapped[str] = mapped_column(db.Text, nullable=True)
    create_time: Mapped[datetime.datetime] = mapped_column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now(cst_tz)
    )

class weibo_Pic_Model(db.Model):
    __tablename__ = 'weibo_Pic'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    url: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    media_id: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    create_time: Mapped[datetime.datetime] = mapped_column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now(cst_tz)
    )

class weibo_Vedio_Model(db.Model):
    __tablename__ = 'weibo_Vedio'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    media_id: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False, default=None)
    introduction: Mapped[str] = mapped_column(db.String, nullable=False, default=None)
    create_time: Mapped[datetime.datetime] = mapped_column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now(cst_tz)
    )

class weibo_wpp_draft_Model(db.Model):
    __tablename__ = 'wpp_draft'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    author: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    media_id: Mapped[str] = mapped_column(db.String, nullable=False, unique=True)
    digest: Mapped[str] = mapped_column(db.String, nullable=False, default=None)
    content: Mapped[str] = mapped_column(db.String, nullable=False, default=None)
    content_source_url: Mapped[str] = mapped_column(db.String, nullable=False, default=None)
    thumb_media_id: Mapped[str] = mapped_column(db.String, nullable=False, default=None)
    create_time: Mapped[datetime.datetime] = mapped_column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now(cst_tz)
    )