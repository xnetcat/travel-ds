SEARCH_QUERY = """
query citySearch($CitySearchRequest: CitySearchRequest!, $ContentSummaryRequest: ContentSummaryRequest!, $PricingSummaryRequest: PricingRequestParameters, $PriceStreamMetaLabRequest: PriceStreamMetaLabRequest) {
  citySearch(CitySearchRequest: $CitySearchRequest) {
    searchResult {
      sortMatrix {
        result {
          fieldId
          sorting {
            sortField
            sortOrder
            sortParams {
              id
            }
          }
          display {
            name
          }
          childMatrix {
            fieldId
            sorting {
              sortField
              sortOrder
              sortParams {
                id
              }
            }
            display {
              name
            }
            childMatrix {
              fieldId
              sorting {
                sortField
                sortOrder
                sortParams {
                  id
                }
              }
              display {
                name
              }
            }
          }
        }
      }
      searchInfo {
        hasSecretDeal
        isComplete
        totalFilteredHotels
        hasEscapesPackage
        searchStatus {
          searchCriteria {
            checkIn
          }
          searchStatus
        }
        objectInfo {
          objectName
          cityName
          cityEnglishName
          countryId
          countryEnglishName
          mapLatitude
          mapLongitude
          mapZoomLevel
          wlPreferredCityName
          wlPreferredCountryName
          cityId
          cityCenterPolygon {
            geoPoints {
              lon
              lat
            }
            touristAreaCenterPoint {
              lon
              lat
            }
          }
        }
      }
      urgencyDetail {
        urgencyScore
      }
      histogram {
        bins {
          numOfElements
          upperBound {
            perNightPerRoom
            perPax
          }
        }
      }
      nhaProbability
    }
    properties(ContentSummaryRequest: $ContentSummaryRequest, PricingSummaryRequest: $PricingSummaryRequest, PriceStreamMetaLabRequest: $PriceStreamMetaLabRequest) {
      propertyId
      sponsoredDetail {
        sponsoredType
        trackingData
        isShowSponsoredFlag
      }
      propertyResultType
      content {
        informationSummary {
          propertyLinks {
            propertyPage
          }
          atmospheres {
            id
            name
          }
          localeName
          defaultName
          displayName
          accommodationType
          awardYear
          hasHostExperience
          nhaSummary {
            hostType
          }
          address {
            country {
              id
              name
            }
            city {
              id
              name
            }
            area {
              id
              name
            }
          }
          propertyType
          rating
          agodaGuaranteeProgram
          remarks {
            renovationInfo {
              renovationType
              year
            }
          }
          spokenLanguages {
            id
          }
          geoInfo {
            latitude
            longitude
          }
        }
        propertyEngagement {
          lastBooking
          peopleLooking
        }
        nonHotelAccommodation {
          masterRooms {
            noOfBathrooms
            noOfBedrooms
            noOfBeds
            roomSizeSqm
            highlightedFacilities
          }
          hostLevel {
            id
            name
          }
          supportedLongStay
        }
        facilities {
          id
        }
        images {
          hotelImages {
            id
            caption
            providerId
            urls {
              key
              value
            }
          }
        }
        reviews {
          contentReview {
            isDefault
            providerId
            demographics {
              groups {
                id
                grades {
                  id
                  score
                }
              }
            }
            summaries {
              recommendationScores {
                recommendationScore
              }
              snippets {
                countryId
                countryCode
                countryName
                date
                demographicId
                demographicName
                reviewer
                reviewRating
                snippet
              }
            }
            cumulative {
              reviewCount
              score
            }
          }
          cumulative {
            reviewCount
            score
          }
        }
        familyFeatures {
          hasChildrenFreePolicy
          isFamilyRoom
          hasMoreThanOneBedroom
          isInterConnectingRoom
          isInfantCottageAvailable
          hasKidsPool
          hasKidsClub
        }
        personalizedInformation {
          childrenFreePolicy {
            fromAge
            toAge
          }
        }
        localInformation {
          landmarks {
            transportation {
              landmarkName
              distanceInM
            }
            topLandmark {
              landmarkName
              distanceInM
            }
            beach {
              landmarkName
              distanceInM
            }
          }
          hasAirportTransfer
        }
        highlight {
          cityCenter {
            distanceFromCityCenter
          }
          favoriteFeatures {
            features {
              id
              title
              category
            }
          }
          hasNearbyPublicTransportation
        }
        rateCategories {
          escapeRateCategories {
            rateCategoryId
            localizedRateCategoryName
          }
        }
      }
      soldOut {
        soldOutPrice {
          averagePrice
        }
      }
      pricing {
        pulseCampaignMetadata {
          promotionTypeId
          webCampaignId
          campaignTypeId
          campaignBadgeText
          campaignBadgeDescText
        }
        isAvailable
        isReady
        benefits
        cheapestRoomOffer {
          agodaCash {
            showBadge
            giftcardGuid
            dayToEarn
            earnId
            percentage
            expiryDay
          }
        }
        isEasyCancel
        isInsiderDeal
        isMultiHotelEligible
        suggestPriceType {
          suggestPrice
        }
        roomBundle {
          bundleId
          bundleType
          saveAmount {
            perNight {
              ...Frag5h5969201ahf53c7a771
            }
          }
        }
        pointmax {
          channelId
          point
        }
        priceChange {
          changePercentage
          searchDate
        }
        payment {
          cancellation {
            cancellationType
            freeCancellationDate
          }
          payLater {
            isEligible
          }
          payAtHotel {
            isEligible
          }
          noCreditCard {
            isEligible
          }
          taxReceipt {
            isEligible
          }
        }
        cheapestStayPackageRatePlans {
          stayPackageType
          ratePlanId
        }
        pricingMessages {
          location
          ids
        }
        suppliersSummaries {
          id
          supplierHotelId
        }
        supplierInfo {
          id
          name
          isAgodaBand
        }
        offers {
          roomOffers {
            room {
              availableRooms
              isPromoEligible
              promotions {
                typeId
                promotionDiscount {
                  value
                }
              }
              supplierId
              corSummary {
                hasCor
                corType
                isOriginal
                hasOwnCOR
                isBlacklistedCor
              }
              localVoucher {
                currencyCode
                amount
              }
              pricing {
                currency
                price {
                  perNight {
                    exclusive {
                      display
                      originalPrice
                    }
                    inclusive {
                      display
                      originalPrice
                    }
                  }
                  perBook {
                    exclusive {
                      display
                      rebatePrice
                      originalPrice
                      autoAppliedPromoDiscount
                    }
                    inclusive {
                      display
                      rebatePrice
                      originalPrice
                      autoAppliedPromoDiscount
                    }
                  }
                  perRoomPerNight {
                    exclusive {
                      display
                      crossedOutPrice
                      rebatePrice
                      pseudoCouponPrice
                      originalPrice
                    }
                    inclusive {
                      display
                      crossedOutPrice
                      rebatePrice
                      pseudoCouponPrice
                      originalPrice
                    }
                  }
                  totalDiscount
                  priceAfterAppliedAgodaCash {
                    perBook {
                      ...Frag63457d3f981dh1bha7j7
                    }
                    perRoomPerNight {
                      ...Frag63457d3f981dh1bha7j7
                    }
                  }
                }
                apsPeek {
                  perRoomPerNight {
                    ...Frag5h5969201ahf53c7a771
                  }
                }
                promotionPricePeek {
                  display {
                    perBook {
                      ...Frag5h5969201ahf53c7a771
                    }
                    perRoomPerNight {
                      ...Frag5h5969201ahf53c7a771
                    }
                    perNight {
                      ...Frag5h5969201ahf53c7a771
                    }
                  }
                  discountType
                  promotionCodeType
                  promotionCode
                  promoAppliedOnFinalPrice
                  childPromotions {
                    campaignId
                  }
                  campaignName
                }
                channelDiscountSummary {
                  channelDiscountBreakdown {
                    display
                    discountPercent
                    channelId
                  }
                }
              }
              uid
              payment {
                cancellation {
                  cancellationType
                }
              }
              discount {
                deals
                channelDiscount
              }
              saveUpTo {
                perRoomPerNight
              }
              benefits {
                id
                targetType
              }
              channel {
                id
              }
              mseRoomSummaries {
                supplierId
                subSupplierId
                pricingSummaries {
                  currency
                  channelDiscountSummary {
                    channelDiscountBreakdown {
                      channelId
                      discountPercent
                      display
                    }
                  }
                  price {
                    perRoomPerNight {
                      exclusive {
                        display
                      }
                      inclusive {
                        display
                      }
                    }
                  }
                }
              }
              agodaCash {
                showBadge
                giftcardGuid
                dayToEarn
                expiryDay
                percentage
              }
              corInfo {
                corBreakdown {
                  taxExPN {
                    ...Fragd95bge9b252003bfbd85
                  }
                  taxInPN {
                    ...Fragd95bge9b252003bfbd85
                  }
                  taxExPRPN {
                    ...Fragd95bge9b252003bfbd85
                  }
                  taxInPRPN {
                    ...Fragd95bge9b252003bfbd85
                  }
                }
                corInfo {
                  corType
                }
              }
              loyaltyDisplay {
                items
              }
              capacity {
                extraBedsAvailable
              }
              pricingMessages {
                formatted {
                  location
                  texts {
                    index
                    text
                  }
                }
              }
              campaign {
                selected {
                  messages {
                    campaignName
                    title
                    titleWithDiscount
                    description
                    linkOutText
                    url
                  }
                }
              }
            }
          }
        }
      }
      metaLab {
        attributes {
          attributeId
          dataType
          value
          version
        }
      }
      enrichment {
        topSellingPoint {
          tspType
          value
        }
        pricingBadges {
          badges
        }
        uniqueSellingPoint {
          rank
          segment
          uspType
          uspPropertyType
        }
        bookingHistory {
          bookingCount {
            count
            timeFrame
          }
        }
        showReviewSnippet
        isPopular
        roomInformation {
          cheapestRoomSizeSqm
          facilities {
            id
            propertyFacilityName
            symbol
          }
        }
      }
      priceBreakerProperties {
        propertyId
        content {
          informationSummary {
            displayName
            rating
            propertyLinks {
              propertyPage
            }
            address {
              area {
                name
              }
              city {
                name
              }
            }
          }
          highlight {
            cityCenter {
              distanceFromCityCenter
              isInsideCityCenter
            }
          }
          reviews {
            contentReview {
              summaries {
                snippets {
                  countryId
                  countryCode
                  countryName
                  date
                  demographicId
                  demographicName
                  reviewer
                  reviewRating
                  snippet
                }
              }
            }
            cumulative {
              score
              reviewCount
            }
          }
          images {
            hotelImages {
              id
              caption
              providerId
              urls {
                key
                value
              }
            }
          }
        }
        pricing {
          isReady
          isAvailable
          offers {
            roomOffers {
              room {
                uid
                pricing {
                  currency
                  price {
                    perRoomPerNight {
                      exclusive {
                        crossedOutPrice
                        display
                      }
                      inclusive {
                        crossedOutPrice
                        display
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    searchEnrichment {
      suppliersInformation {
        supplierId
        supplierName
        isAgodaBand
      }
    }
    aggregation {
      matrixGroupResults {
        matrixGroup
        matrixItemResults {
          id
          name
          count
          filterKey
          filterRequestType
          extraDataResults {
            text
            matrixExtraDataType
          }
        }
      }
    }
  }
}

fragment Frag63457d3f981dh1bha7j7 on DisplayPrice {
  exclusive
  allInclusive
}

fragment Frag5h5969201ahf53c7a771 on DFDisplayPrice {
  exclusive
  allInclusive
}

fragment Fragd95bge9b252003bfbd85 on DFCorBreakdownItem {
  price
  id
}
"""
